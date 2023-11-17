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

    # Operator
    (r'\<', 'TAG_OPEN'),
    (r'\>', 'TAG_CLOSE'),
    (r'\/', 'CLOSE_CODE'),
    
    # Type
    (r'[0-9]', 'INT'),
    
    # Keywords
    (r'\bhtml\b', 'HTML'),
    (r'\bhead\b', 'HEAD'),
    (r'\bbody\b', 'BODY'),
    (r'\btitle\b', 'TITLE'),
    (r'\blink\b', 'LINK'),
    (r'\bscript\b', 'SCRIPT'),
    (r'\bh1\b', 'H1'),
    (r'\bh2\b', 'H2'),
    (r'\bh3\b', 'H3'),
    (r'\bh4\b', 'H4'),
    (r'\bh5\b', 'H5'),
    (r'\bh6\b', 'H6'),
    (r'\bp\b', 'PARAGRAPH'),
    (r'\bbr\b', 'BREAK'),
    (r'\bem\b', 'EMPHASIS'),
    (r'\bb\b', 'BOLD'),
    (r'\babbr\b', 'ABBREVIATION'),
    (r'\bstrong\b', 'STRONG'),
    (r'\bsmall\b', 'SMALL'),
    (r'\bhr\b', 'HORIZONTAL_RULE'),
    (r'\bdiv\b', 'DIV'),
    (r'\ba\b', 'ANCHOR'),
    (r'\bimg\b', 'IMAGE'),
    (r'\bbutton\b', 'BUTTON'),
    (r'\bform\b', 'FORM'),
    (r'\binput\b', 'INPUT'),
    (r'\btable\b', 'TABLE'),
    (r'\btr\b', 'TABLE_ROW'),
    (r'\btd\b', 'TABLE_DATA'),
    (r'\bth\b', 'TABLE_HEADER'),
    
    # Untuk Variabel
    (r'[A-Za-z_$][A-Za-z0-9_$]*', 'VAR'),
]

def createToken(text):
    # Read file
    path = "html\\" + text
    file = open(path, encoding="utf8")
    characters = file.read()
    file.close()
    print(characters)
    
    tokens = lex(characters, token_rules)
    tokenResult = []
    
    for token in tokens:
        tokenResult.append(token)
        
    return tokenResult