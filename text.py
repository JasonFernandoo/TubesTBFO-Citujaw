from FileHandler import FileHandler
import time
import re

def listInput(input):
    parsed_list = re.findall(r"att|[a-zA-Z1-9]+|id|=|\"|<|>|/|[^<>/\"\s]+", input)
    return parsed_list

def compute_pda(input_string, parsed_lines):
    stack = []
    input_string = listInput(input_string)
    input_string.append('$')
    init_stack_symbol = parsed_lines['initial_stack']
    stack.append(init_stack_symbol)
    final_states = parsed_lines['final_states']
    initial_state = parsed_lines['initial_state']
    productions = parsed_lines['productions']

    current_stack_symbol = init_stack_symbol
    current_state = initial_state
    
    print('State\tInput\tStack\tMove')
    print('{}\t {}\t {}\t ({}, {})'.format(current_state, '_', 'Z', current_stack_symbol, stack))
    for i in range (len(input_string)):
        for production in productions:
            if ((production[0] == current_state) and (str(production[1]) == str(input_string[i])) and (production[2] == current_stack_symbol)):
                current_state = production[3]
                if (len(listInput(production[4])) ==  1):
                    if (production[4] != '$'):
                        stack.pop()
                        if (input_string[i] == "id" or input_string[i] == "class" or input_string[i] == "style" or input_string[i] == "src" or input_string[i] == "href" 
                            or input_string[i] == "alt" or input_string[i] == "type" or input_string[i] == '=' or input_string[i] == '"'):
                            stack.append("att")
                        else:
                            stack.append(input_string[i])
                    else:
                        stack.pop()
                        break
                elif (len(listInput(production[4])) ==  2):
                    if (input_string[i] == "id" or input_string[i] == "class" or input_string[i] == "style" or input_string[i] == "src" or input_string[i] == "href"
                        or input_string[i] == "alt" or input_string[i] == "type" or input_string[i] == '=' or input_string[i] == '"'):
                            stack.append("att")
                    else:
                        stack.append(input_string[i])
                
        previous_stack_symbol = current_stack_symbol
        current_stack_symbol = stack[len(stack) - 1]

        print('{}\t {}\t {}\t ({}, {})'.format(current_state, input_string[i], previous_stack_symbol, current_stack_symbol, stack))

    if (current_state in final_states):
        print('String accepted by PDA.')
    else:
        print('String rejected by PDA.')

def main():
    fh = FileHandler()
    automata_file_path = "pda/pda.txt"
    # automata_file_path = input('Enter the automata file path: ')
    lines = fh.readFile(automata_file_path)
    print('Reading Automata File')
    print('Automata File Successfully Read')

    input_string = input('Enter input String: ')
    input_string = input_string.rstrip()
    print('Loading Details from Automata File: ')

    parsed_lines = fh.parseFile(lines)
    print('States: ', parsed_lines['states'])
    print('Input Symbols: ', parsed_lines['input_symbols'])
    print('Stack Symbols: ', parsed_lines['stack_symbols'])
    print('Initial State: ', parsed_lines['initial_state'])
    print('Initial Stack Symbol: ', parsed_lines['initial_stack'])
    print('Final States: ', parsed_lines['final_states'])
    print('Productions List:')
    for production in parsed_lines['productions']:
        print('\t', production)

    print('Details loaded')
    print('Computing the Transition Table:')
    compute_pda(input_string, parsed_lines)

if __name__ == '__main__':
    main()
