from backtracking import *


print("Matching bc with the regex a|bc returns..." + str(regex_matching("bc", "a|bc")))
print("\n")
print("Matching aaaaa with the regex (a*)?aaaaa returns..." + str(regex_matching("bc", "a|bc")))
print("\n")
print("Matching aab with the regex aab|a?aab returns..." + str(regex_matching("aab", "a?aab")))
print("\n")
print("Matching aaaaaaba with the regex (aa)*aaba returns..." + str(regex_matching("aaaaaaba", "(aa)*aaba")))
print("\n")
print("Matching ccccddee with the regex ((abc)*|(a|(b|c)*d+))(def|e) returns..." + str(regex_matching("ccccddee", "((abc)*|(a|(b|c)*d+))(def|e)")))
print("\n")
print("Matching b with the regex a*b returns..." + str(regex_matching("b", "a*b")))
print("\n")
print("Matching aabadddehijk with the regex aaba(ad)*|hi|(d*e)|g(hi)jk returns..." + str(regex_matching("aabadddehijk", "aaba(ad)*|hi|(d*e)|g(hi)jk")))
print("\n")
print("Matching add with the regex (ad)*d* returns..." + str(regex_matching("add", "(ad)*d*")))
print("\n")
print("Matching xxxxxxxxxxxxxxxxxxxxxxxxxxxxy with the regex (x+x+)+y returns..." + str(regex_matching("xxxxxxxxxxxxxxxxxxxxxxxxxxxxy", "(x+x+)+y")))
print("\n")
print("Matching xxxxxxxxxxxxxxxxxxxxxxxxxxxx with the regex (x+x+)+y returns..." + str(regex_matching("xxxxxxxxxxxxxxxxxxxxxxxxxxxx", "(x+x+)+y")))
print("\n")

roster = ["rick", "puneet", "bodik", "aaron"]
for i in roster:
    if regex_matching(i, "b+o+d+i+k+"):
	print(str(i) + " is a professor")
    else:
	print(str(i) + " is a student")

print("\n")

#Valid regex, also demonstrates potential for desugaring other regexs in our DSL

any_letter = "(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)*"
any_number = "(0|1|2|3|4|5|6|7|8|9)*"
email_regex = any_letter + "_?" + any_letter + any_number +"@" + any_letter + "." + "(com)|(edu)|(net)"

print("Email Regex: " + str(email_regex))

emails = ["rickbhardwaj1993@gmail.com", "bodik@berkeley.edu", "malware@ch.cm"]

for i in emails:
    if regex_matching(i, email_regex):
	print(str(i) + " is a valid email")
    else:
	print(str(i) + " is NOT a valid email")
print("\n")
