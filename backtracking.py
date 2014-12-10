# For the regex (abc|de)x

def match(s, patt):
    matches = patt(s, 1)
    for pos in matches:
        if pos == len(s)+1:
            return True
        return False

def prim(st):
    def prim_helper(s, pos):
        if pos+len(st) < len(s) and s[pos:pos+len(st)] == st:
            yield pos + len(st)

    return lambda s, pos: prim_helper(s, pos)

#seq(prim("h"), prim("ello")) 
def seq(patt1, patt2):
    def seq_helper(s, pos):
        for npos in patt1(s, pos):
            patt2(s, npos)
    return lambda s, pos: seq_helper(s, pos)


def alt(patt1, patt2):
    def alt_helper(s, pos):
        patt1(s, pos)
        patt2(s, pos)
    return lambda s, pos: alt_helper(s, pos)


patt = seq(prim("abc"), prim("def"))
#patt = seq(alt(prim("abc"), prim("de")), prim("x"))
match("def", patt)
