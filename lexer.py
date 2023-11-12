import os
import re
import sys

def lex(text, token_rules):
    pos = 0
    line = 1 
    tokens = []

    while (pos < len(text)):
        if text[pos] == '\n':
            line += 1

        flag = None
        for pattern, tag in token_rules:
            regex = re.compile(pattern)

            flag = regex.match(text, pos)

            if flag:
                if tag:
                    token = (tag, flag.group(0), line) 
                    tokens.append(token)
                break

        if not flag:
            print("SYNTAX ERROR !!!")
            print(f'Error Expression at line {line}: {text.splitlines()[line - 1]}')
            sys.exit(1)
        else:
            pos = flag.end(0)

    return tokens

token_rules = [

]

def createToken(text):
    # Read file
    file = open(text, encoding="utf8")
    characters = file.read()
    file.close()
    print(characters)