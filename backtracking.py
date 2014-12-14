from parser import parse
from parser import Node

# For the regex (abc|de)x

def match(s, patt):
    matches = patt(s, 0)
    for pos in matches:
        print(pos)
        if pos == len(s):
            print True
            return True
    print False
    return False

def prim(st):
    def prim_helper(s, pos):
        if pos+len(st) <= len(s) and s[pos:pos+len(st)] == st:
            yield pos + len(st)

    return lambda s, pos: prim_helper(s, pos)

#Kleene Primitive
'''
def kleene(patt1):
    def kleene_helper(s, pos):
	kleene_pos = pos
	while kleene_pos+len(st) <= len(s) and s[kleene_pos:kleene_pos+len(st)] == st:
	    kleene_pos += len(st)
	    yield kleene_pos
    return lambda s, pos: kleene_helper(s, pos)
''' 
  

#seq(prim("h"), prim("ello")) 
def seq(patt1, patt2):
    def seq_helper(s, pos):
        for npos in patt1(s, pos):
            for mpos in patt2(s, npos):
                yield mpos
    return lambda s, pos: seq_helper(s, pos)



def alt(patt1, patt2):
    print("patt1 " + str(patt1))
    print("patt2 " + str(patt2))
    def alt_helper(s, pos):
        for apos in patt1(s, pos):
	    yield apos
        for bpos in patt2(s, pos):
	    yield bpos
    return lambda s, pos: alt_helper(s, pos)

def kleene(patt1):
    def kleene_helper(s, pos):
	kleene_match = True
	while kleene_match:
	    kleene_match = False
	    for apos in patt1(s, pos):	
	    	kleene_match = True
		pos = apos
	        yield pos
    return lambda s, pos: kleene_helper(s, pos)


def plus(patt1):
    def plus_helper(s, pos):
	plus_match = True
        orig_pos = pos
	while plus_match:
	    plus_match = False
	    for apos in patt1(s, pos):	
	    	plus_match = True
		pos = apos
                if pos != orig_pos:
	            yield pos
    return lambda s, pos: plus_helper(s, pos)

def call_ast(ast):
    ret_func = None
    if(ast.regex == "prim"):
	ret_func = prim(ast.prim_value)

    if(ast.regex == "seq"):
	ret_func = seq(call_ast(ast.left), call_ast(ast.right))  	

    if(ast.regex == "alt"):
	ret_func = alt(call_ast(ast.left), call_ast(ast.right)) 

    if(ast.regex == "kleene"):
	ret_func = kleene(call_ast(ast.child)) 

    if(ast.regex == "plus"):
	ret_func = plus(call_ast(ast.child)) 

    return ret_func

patt = seq(plus(prim("a")), prim("aab"))
match("aab", patt)
	
'''
patt = alt(prim("science"), prim("history"))

match("history", patt)

ast = parse(("(science)|(history)"))

parr = call_ast(ast)

match("history", parr)
'''
