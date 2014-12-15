class Node(object):
    def __init__(self):
        self.regex = None
        self.prim_value = None
        self.left = None
        self.right = None
        self.child = None
    def __str__(self):
        if self.regex == None:
            return "None"
        elif self.regex == "prim":
            return "prim(\"" + self.prim_value + "\")"
        elif self.regex == "seq" or self.regex == "alt":
            return self.regex + "(" + str(self.left) + ", " + str(self.right) + ")"
        else:
            return self.regex + "(" + str(self.child) + ")"

def parse(tokens, trail_prim = ""):
    node = Node()
    i = len(tokens) - 1
    
    #check if there is a trailing prim, concatenate onto existing stack or return collected prims
    if not is_rep_mod(tokens[i]) and tokens[i] != ")" and in_alt_node(i, tokens) < 0:
        trail_prim = tokens[i] + trail_prim
        if i == 0:
            node.regex = "prim"
            node.prim_value = trail_prim
        else:
            node = parse(tokens[:i], trail_prim)
    
    #add trailing prim back on if it exists
    elif trail_prim != "":
        prim = Node()
        prim.regex = "prim"
        prim.prim_value = trail_prim
        node.regex = "seq"
        node.left = parse(tokens)
        node.right = prim

    #redundant parenthesis
    elif tokens[i] == ")" and matching_open(i, tokens) == 0:
        node = parse(tokens[1:i])

    #simple sequence, no alt
    elif in_alt_node(i, tokens) < 0:
        node.regex = "seq"
        offset = 0
        if is_rep_mod(tokens[i]):
            offset = 1
            temp = Node()
            temp.regex = rep_str[tokens[i]]
        i_open = i - offset
        if tokens[i_open] == ")":
            i_open = matching_open(i_open, tokens)
        if i_open != 0:
            node.left = parse(tokens[:i_open])
        if offset == 1:
            temp.child = parse(tokens[i_open:i])
            if i_open == 0:
                node = temp
            else:
                node.right = temp
        else:
            if i_open == 0:
                node = parse(tokens[i_open:])
            else:
                node.right = parse(tokens[i_open:])

    #with alts
    else:
        alt = Node()
        alt.regex = "alt"
        i_left = in_alt_node(i, tokens)
        start = first_alt(i, tokens)
        alt.right = parse(tokens[i_left + 2:])
        alt.left = parse(tokens[start:i_left+1])

        if start == 0:
            node = alt
        else:
            offset = 0
            if is_rep_mod(tokens[start-1]):
                offset = 1
            i_open = start -1 - offset
            if tokens[i_open] == ")":
                i_open = matching_open(i_open, tokens)
            node.regex = "seq"
            node.left = parse(tokens[:start])
            node.right = alt
    return node

#dict of repetition symbol string names
rep_str = {"*":"kleene", "+":"plus", "?":"ques"}

#given index of closing parens, returns matching open parens index
def matching_open(i, seq):
    count = 1
    while count != 0:
        i -= 1
        if seq[i] == ")":
            count += 1
        elif seq[i] == "(":
            count -= 1
    return i

#given character, determines if it is either *, +, or ?
def is_rep_mod(token):
    return token == "*" or token == "+" or token == "?"

#given index and sequence, returns index of other side of alt or 0
def in_alt_node(i, seq):
    offset = 0
    if is_rep_mod(seq[i]):
        offset = 1
    i_open = i - offset
    if seq[i - offset] == ")":
        i_open = matching_open(i - offset, seq)
    if seq[i_open - 1] == "|":
        return i_open - 2
    else:
        return -1

#given index to right side of alt, returns index of beginning of whole alt chain
def first_alt(i, seq):
    i_left = in_alt_node(i, seq)
    while True:
        if in_alt_node(i_left, seq) < 0:
            break
        else:
            i_left = in_alt_node(i_left, seq)
    offset = 0
    if is_rep_mod(seq[i_left]):
        offset = 1
    if seq[i_left - offset] == ")":
        return matching_open(i_left - offset, seq)
    return i_left - offset

reg = "aaba(ad)*|hi|(d*e)|g(hi)jk"
ast = parse(reg)
print(str(ast))