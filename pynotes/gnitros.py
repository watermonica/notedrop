import re
string = input()
pattern = "[a-z]", "[A-Z]", "[13579]", "[02468]"
print(''.join(map(lambda x: ''.join(sorted(re.findall(x, string))), pattern)))
