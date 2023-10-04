from typing import Callable

def p1(inp_str: str):
    return inp_str.replace('$$', '*')

def p2(inp_str: str):
    return inp_str.replace('*$', '*')

def p3(inp_str: str):
    i = inp_str.find('*')
    if i == -1:
        raise ValueError('No * found')
    _inp_str = inp_str[:i] + inp_str[i+1] + '*' + inp_str[i+2:]
    return _inp_str

def p4(input: str):
    return input.replace('*', '')

def p5(inp_str: str):
    i = inp_str.find('$')
    if i == -1 or inp_str[i+1] == '$' or inp_str[i+2] == '$':
        raise ValueError('No valid $ found')
    _inp_str = inp_str[:i] + inp_str[i+2] + '$' + inp_str[i+1] + inp_str[i+3:]
    return _inp_str

def p6(inp_str: str):
    return '$' + inp_str

def match_rule(input: str, ruleset: dict[str, Callable[[str], str]]):
    for rule_name, rule in ruleset.items():
        try: 
            _inp = rule(input)
            if _inp != input:
                return rule_name
            else: 
                continue
        except (ValueError, KeyError, IndexError):
            continue
    return 'P4'

def main():
    INPUT = 'ABCD'
    _RULESET =  [
        'P1: $$ -> *',
        'P2: *$ -> *',
        'P3: *x -> x*',
        'P4: * -> null & halt',
        'P5: $xy -> y$x',
        'P6: null -> $',
        ]
    ruleset = {
        'P1': p1,
        'P2': p2,
        'P3': p3,
        'P4': p4,
        'P5': p5,
        'P6': p6,
    }
    print(f'Input: {INPUT}')
    print(f'Ruleset:')
    for rule in _RULESET:
        print(f'{rule}')
    print('------------------')
    print('Rule\tInput\tOutput')
    print('------------------')
    rule = None
    while rule != 'P4':
        rule = match_rule(INPUT, ruleset)
        print(f'{rule}\t{INPUT}\t{ruleset[rule](INPUT)}')
        INPUT = ruleset[rule](INPUT)
    
    print(f'{rule}\t{INPUT}\t{ruleset[rule](INPUT)}')



if __name__ == '__main__':
    main()