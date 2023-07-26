from collections import deque


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
    if a <= 0 or b <= 0 or a < current[0] or b < current[1]:
        return False
    return True

def get_path_from_transitions(transitions: list[tuple[tuple[int, int], tuple[int, int]]], final_state: tuple[int, int]):
    path: list[tuple[int, int]] = list()
    current_state = final_state
    transitions = list(set(transitions))
    # This sort ensures that the minimal filled ones are at the front, giving a shorter reverse path (more closer to (0, 0) )
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
    mark: set[tuple[int, int]] = set()
    queue: deque[tuple[int, int]] = deque()
    transitions: list[tuple[tuple[int, int], tuple[int, int]]] = list()
    path: list[tuple[int, int]] = list()
    
    queue.append((0, 0))
    
    while len(queue) > 0:
        current = queue.popleft()
        if current in mark:
            # Already visited state
            continue
        if not is_valid(a, b, current):
            # Invalid State
            continue
        
        # path.append(current)
        
        mark.add(current) # Mark the current state as visited.
        
        if current[0] == target or current[1] == target:
            # Solution found
            solution_found = True
            if current[0] == target:
                path.append((current[0], 0))
                transitions.append((current, (current[0], 0)))
            else:
                path.append((0, current[1]))
                transitions.append((current, (0, current[1])))
            break
        
        # Incase we didn't find solution
        queue.append((a, current[1])) # R1: Fill the first jug 
        transitions.append((current, (a, current[1])))
        queue.append((current[0], b)) # R2: Fill the second jug
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
        
        queue.append((0, current[1])) # R5 : Empty first jug
        transitions.append((current, (0, current[1])))
        queue.append((current[0], 0)) # R6 : Empty second jug
        transitions.append((current, (current[0], 0)))
    
    _p = path.pop()
    path = get_path_from_transitions(transitions, _p)
    path = path + [_p]
    
    return solution_exists, solution_found, path

if __name__ == "__main__":
    se, sf, p = water_jug_bfs(int(input("A:")), int(input("B:")), int(input("T:")))
    if se == sf == True: # Check to make sure that errors don't compromise answer
        _pl = len(p)
        for pe, idx in enumerate(p):
            print(f"{idx[0]} {idx[1]}", end="")
            if pe != _pl - 1:
                print(" -> ", end="")
    else:
        print("No solution exists")
        exit(1)