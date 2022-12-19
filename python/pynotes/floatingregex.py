import re

for _ in range(int(input())):
    x = [print('True') if bool(re.search(r'^[-+]?[0-9]*\.[0-9]+$', input())) else print('False')]


# VISIT https://www.programiz.com/python-programming/regex
