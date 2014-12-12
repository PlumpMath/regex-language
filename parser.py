class Node(object):
    def __init__(self):
        self.regex = None
	self.prim_value = None
        self.left = None
	self.right = None
        self.child = None

def parse(tokens):
    node = Node()
    #seq = tokens.find(")")
    paren_counter = [0, False]
    seq = 0
    for token in tokens:
	if(token == "("):
	    paren_counter[0] += 1 	
	    paren_counter[1] = True	

	if(token == ")"):
	    paren_counter[0] -= 1
	
	if(paren_counter[0] == 0 and paren_counter[1] == True):
	    break
	seq += 1

#    def process(s):
#	if s.count("(") > s.count(")"):
#	   s = s[1:]
#	if s.count("(") < s.count(")"):
#	   s = s[:-1]
#	return s


    if not "(" in tokens and not ")" in tokens and not "|" in tokens:
        if "*" in tokens:
            node.regex = "kleene"
            node.child = parse(tokens[:-1])
        elif "+" in tokens:
            node.regex = "plus"
            node.child = parse(tokens[:-1])
        else:
            node.regex = "prim"
	    node.prim_value = tokens

    if seq:
	if seq == len(tokens) - 1:
	    node = parse(tokens[1:-1])
	if seq < len(tokens) - 1:
	    if tokens[seq+1] == "(": 
		node.regex = "seq"
		node.left = parse(tokens[:seq+1])
		node.right = parse(tokens[seq+1:])
	    if tokens[seq+1] == "|": 
		node.regex = "alt"
		print("first half " + tokens[:seq+1])
		node.left = parse(tokens[:seq+1])
		print("second half " + tokens[seq+2:])
		node.right = parse(tokens[seq+2:])
	
    return node
'''
inp = "((a)|(c*))|((b))"
ast = parse(inp)
print(ast.regex)
print(ast.left.regex)
print(ast.left.left.regex)
print(ast.left.right.regex)
print(ast.right.regex)
'''
