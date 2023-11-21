from FileHandler import FileHandler
import time

def compute_pda(input_string, parsed_lines):
    stack = []
    input_string += '$'
    init_stack_symbol = parsed_lines['initial_stack']
    stack.append(init_stack_symbol)
    final_states = parsed_lines['final_states']
    initial_state = parsed_lines['initial_state']
    productions = parsed_lines['productions']

    current_stack_symbol = init_stack_symbol
    current_state = initial_state

    print('State\tInput\tStack\tMove')
    print('{}\t {}\t {}\t ({}, {})'.format(current_state, '_', 'Z', current_stack_symbol, stack))
    for char in input_string:
        for production in productions:
            if ((production[0] == current_state) and (production[1] == char) and (production[2] == current_stack_symbol)):
                current_state = production[3]
                if (len(production[4]) == 2):
                    stack.append(char)
                elif (len(production[4]) == 3):
                    stack.append(char)
                    stack.append(char)
                elif ((production[4] == '$') and (len(stack) != 1)):
                    stack.pop()
                    break
        previous_stack_symbol = current_stack_symbol
        current_stack_symbol = stack[len(stack) - 1]
        print('{}\t {}\t {}\t ({}, {})'.format(current_state, char, previous_stack_symbol, current_stack_symbol, stack))

    if (current_state in final_states):
        print('String accepted by PDA.')
    else:
        print('String rejected by PDA.')

def main():
    fh = FileHandler()
    automata_file_path = "pda/pdajb.txt"
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
