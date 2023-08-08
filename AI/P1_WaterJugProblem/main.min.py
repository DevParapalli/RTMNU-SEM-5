from collections import deque

__author__ = "Devansh Parapalli"

def gcd(a, b):
    res = min(a, b)
    while res > 0:
        if a % res == 0 and b % res == 0:
            return res
        res -= 1
    raise ValueError("No GCD found")

def is_solvable(a, b, target):
    if a + b < target:
        return False
    if (a == 0 and b == 0):
        return target == 0
    if (target % gcd(a, b) == 0):
        return True
    return False

def is_valid(a, b, current):
    if a < 0 or b < 0 or a < current[0] or b < current[1]:
        return False
    return True

def get_path_from_transitions(transitions, final_state):
    path = list()
    current_state = final_state
    transitions = list(set(transitions))
    transitions.sort(key=lambda x: x[0][0] + x[0][1])
    while current_state != (0, 0):
        for i in transitions:
            if i[1] == current_state and i[0] not in path:
                path.append(i[0])
                current_state = i[0]
                break
    
    path.reverse()
    return path

def water_jug_bfs(a, b, target):
    solution_exists = is_solvable(a, b, target)
    if not solution_exists:
        raise ValueError("No solution exists")
    solution_found = False
    mark = set()
    queue = deque()
    transitions = list()
    path = list()
    
    queue.append((0, 0))
    
    while len(queue) > 0:
        current = queue.popleft()
        if current in mark:
            continue
        if not is_valid(a, b, current):
            continue
        
        mark.add(current) 
        
        if current[0] == target or current[1] == target:
            solution_found = True
            if current[0] == target:
                path.append((current[0], 0))
                transitions.append((current, (current[0], 0)))
            else:
                path.append((0, current[1]))
                transitions.append((current, (0, current[1])))
            break
        
        # R1: Fill the first jug
        queue.append((a, current[1])) 
        transitions.append((current, (a, current[1])))
        # R2: Fill the second jug
        queue.append((current[0], b)) 
        transitions.append((current, (current[0], b)))
        # R3: Pour from A to B
        check_current = (current[0] - (b - current[1]), b) if current[0] > b - current[1] else (0, current[0] + current[1])
        if is_valid(a, b, check_current):
            queue.append(check_current)
            transitions.append((current, check_current))
        # R4: Pour from B to A
        check_current = (a, current[1] - (a - current[0])) if current[1] > a - current[0] else (current[0] + current[1], 0)
        if is_valid(a, b, check_current):
            queue.append(check_current)
            transitions.append((current, check_current))
        # R5 : Empty first jug
        queue.append((0, current[1])) 
        transitions.append((current, (0, current[1])))
        # R6 : Empty second jug
        queue.append((current[0], 0)) 
        transitions.append((current, (current[0], 0)))
    
    _p = path.pop()
    path = get_path_from_transitions(transitions, _p)
    path = path + [_p]
    
    return solution_exists, solution_found, path

if __name__ == "__main__":
    se, sf, p = water_jug_bfs(int(input("A:")), int(input("B:")), int(input("T:")))
    if se == sf == True: # Check to make sure that errors don't compromise answer
        pl = len(p)
        for idx, pe  in enumerate(p):
            print(f"{pe[0]} {pe[1]}", end="")
            if idx != pl - 1:
                print(" -> ", end="")
        print()
    else:
        print("No solution exists")
        exit(1)