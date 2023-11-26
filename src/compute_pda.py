import argparse
import os
import time
import re
import sys

def loader():
    chars = "/—\\|"
    for _ in range(5):
        for char in chars:
            sys.stdout.write('\r' + 'Loading ' + char)
            sys.stdout.flush()
            time.sleep(0.1)
    print()

def listInput(input):
    parsed_list = re.findall(r"att|[a-zA-Z1-9]+|<div>|</div>|=|\"|<|>|/|[^<>/\"\s]+", input)
    return parsed_list

def parse_pda_file(lines):
    ''' Line 1: Total States
            Line 2: Input Word Symbols
            Line 3: Stack Symbols
            Line 4: Initial State Symbol
            Line 5: Initial Stack Symbol
            Line 6: List of Final States
            Line 7 and onwards: Productions in form of
                (Current State, Current Input Symbol, Current Top of Stack, Next State, Push/Pop Operation Symbol)
        '''
    states = lines[0].rstrip().split()
    input_symbols = lines[1].rstrip().split()
    stack_symbols = lines[2].rstrip().split()
    initial_state = lines[3]
    initial_stack = lines[4][0]
    final_states = lines[5].rstrip().split()
    productions = lines[6:]
    for i in range(len(productions)):
        productions[i] = productions[i].rstrip().split()

    parsed_lines = {
        'states': states,
        'input_symbols': input_symbols,
        'stack_symbols': stack_symbols,
        'initial_state': initial_state,
        'initial_stack': initial_stack,
        'final_states': final_states,
        'productions': productions
    }
    return parsed_lines

def parse_html_file(lines):
    html_content = ''.join(lines)
    return html_content

def compute_pda(input_string, parsed_lines):
    stack = []
    input_string = parse_html_file(input_string)
    #parsed_lines = parse_file(parsed_lines)
    input_string = listInput(input_string)
    input_string.append('$')
    init_stack_symbol = parsed_lines['initial_stack']
    stack.append(init_stack_symbol)
    final_states = parsed_lines['final_states']
    initial_state = parsed_lines['initial_state']
    productions = parsed_lines['productions']

    current_stack_symbol = init_stack_symbol
    current_state = initial_state
    
    # print('State\tInput\tStack\tMove')
    # print('{}\t {}\t {}\t ({}, {})'.format(current_state, '_', 'Z', current_stack_symbol, stack))
    for i in range (len(input_string)):
        for production in productions:
            if ((production[0] == current_state) and (str(production[1]) == str(input_string[i])) and (production[2] == current_stack_symbol)):
                current_state = production[3]
                if (len(listInput(production[4])) ==  1):
                    if (production[4] != '$'):
                        stack.pop()
                        if (input_string[i] == "id" or input_string[i] == "class" or input_string[i] == "style" or input_string[i] == "src" or input_string[i] == "href" 
                            or input_string[i] == "alt" or input_string[i] == "type"):
                            stack.append("att")
                        else:
                            stack.append(input_string[i])
                    elif (production[4] == '$'):
                        stack.pop()
                        break
                elif (len(listInput(production[4])) ==  2):
                    if (input_string[i] == '"'):
                            stack.append(input_string[i])
                    if (input_string[i] == "id" or input_string[i] == "class" or input_string[i] == "style" or input_string[i] == "src" or input_string[i] == "href"
                        or input_string[i] == "alt" or input_string[i] == "type" or input_string[i] == '"'):
                            stack.append("att")
                    else:
                        stack.append(input_string[i])
                
        previous_stack_symbol = current_stack_symbol
        current_stack_symbol = stack[len(stack) - 1]

        # print('{}\t {}\t {}\t ({}, {})'.format(current_state, input_string[i], previous_stack_symbol, current_stack_symbol, stack))

    if (current_state in final_states):
        print('String accepted by PDA.')
    else:
        print('String rejected by PDA.')

def main():
    parser = argparse.ArgumentParser(description='Process HTML input with PDA')
    parser.add_argument('automata_file', help='Automata file name')
    parser.add_argument('html_file', help='HTML file name')

    args = parser.parse_args()

    automata_folder = "../pda/"
    html_folder = "../test/"

    automata_file_path = os.path.join(automata_folder, args.automata_file)
    html_file_path = os.path.join(html_folder, args.html_file)

    # Reading automata file
    parsed_lines = []
    try:
        with open(automata_file_path, 'r') as file:
            parsed_lines = [line.rstrip() for line in file]
    except FileNotFoundError:
        print(f'{automata_file_path}: File was not found.')
        exit(0)
    except IOError as e:
        print(f'Error reading {automata_file_path}: {e}')
        exit(0)

    # Reading HTML file
    lines = []
    try:
        with open(html_file_path, 'r') as html_file:
            lines = [line.rstrip() for line in html_file]
            html_content = ''.join(lines)
    except FileNotFoundError:
        print(f'{html_file_path}: File was not found.')
        exit(0)
    except IOError as e:
        print(f'Error reading {html_file_path}: {e}')
        exit(0)

    try:
        with open(html_file_path, 'r') as html_file:
            content = html_file.read()
    except FileNotFoundError:
        print(f'{html_file_path}: File was not found.')
        exit(0)
    except IOError as e:
        print(f'Error reading {html_file_path}: {e}')
        exit(0)

    parsed_lines = parse_pda_file(parsed_lines)
    loader()
    print('Details loaded')
    print()
    print(content)
    print()
    print('Computing the Transition Table:')
    loader()
    compute_pda(html_content, parsed_lines)