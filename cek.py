import re

def listInput(input):
    parsed_list = re.findall(r"att|[a-zA-Z]+|id|=|\"|<|>|/|[^<>/\"\s]+", input)
    return parsed_list

print((listInput('html id="tes"')))