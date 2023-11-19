import os
import re
import sys

def lex(html):
    stack = []
    i = 0
    while i < len(html):
        char = html[i]

        if char == '<':
            if html.startswith('!--', i + 1) or html.startswith('?', i + 1) or html.startswith('![CDATA[', i + 1):
                end = html.find('-->', i + 1) if html.startswith('!--', i + 1) else \
                    html.find('?>', i + 1) if html.startswith('?', i + 1) else \
                    html.find(']]>', i + 1)
                if end == -1:
                    return False
                i = end + 3 if html.startswith('!', i + 1) else end
            else:
                tag_end = html.find('>', i)
                if tag_end == -1:
                    return False

                tag_content = html[i + 1:tag_end]
                if tag_content.startswith('/'):
                    if not stack or stack.pop() != tag_content[1:]:
                        return False
                else:
                    tag_name, _, _ = tag_content.partition(' ')
                    if tag_name.endswith('/'):
                        tag_name = tag_name[:-1]
                    stack.append(tag_name)

                i = tag_end + 1
        else:
            i += 1

    return len(stack) == 0

def checkhtml(html):
    html = "html\\" + html

    file = open(html, encoding="utf8")
    characters = file.read()
    file.close()
    print(characters)

    if characters:
        # Test the HTML checker with HTML content read from a file
        is_valid = lex(characters)

        if is_valid:
            print()
            print("Accepted !!!")
        else:
            print()
            print("SYNTAX ERROR !!!")


# def lex(text, token_rules):
#     pos = 0
#     line = 1 
#     tokens = []

#     while (pos < len(text)):
#         if text[pos] == '\n':
#             line += 1

#         flag = None
#         for pattern, tag in token_rules:
#             regex = re.compile(pattern)

#             flag = regex.match(text, pos)

#             if flag:
#                 if tag:
#                     token = (tag, flag.group(0), line) 
#                     tokens.append(token)
#                 break

#         if not flag:
#             print("SYNTAX ERROR !!!")
#             print(f'Error Expression at line {line}: {text.splitlines()[line - 1]}')
#             sys.exit(1)
#         else:
#             pos = flag.end(0)

#     return tokens

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