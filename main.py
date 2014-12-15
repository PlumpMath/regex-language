from backtracking import *

print(regex_matching("bc", "a|bc"))
print(regex_matching("aab", "a?aab"))
print(regex_matching("ccccddee", "((abc)*|(a|(b|c)*d+))(def|e)"))
print(regex_matching("b", "a*b"))
print(regex_matching("aabadddehijk", "aaba(ad)*|hi|(d*e)|g(hi)jk"))
print(regex_matching("add", "(ad)*d*"))

roster = ["rick", "puneet", "bodik", "aaron"]
for i in roster:
    if regex_matching(i, "b+o+d+i+k+"):
	print "Found professor"
    else:
	print "Found student"

#Valid regex, also demonstrates potential for desugaring other regexs
any_letter = "(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)*"
email_regex = any_letter + "_?" + any_letter + "@" + any_letter + "." + "(com)|(edu)|(net)"

emails = ["rickbhardwaj@gmail.com", "bodik@berkeley.edu", "malware@ch.cm"]

for i in emails:
    if regex_matching(i, email_regex):
	print(str(i) + " is a valid email")
    else:
	print(str(i) + " is NOT a valid email")
