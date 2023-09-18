from collections import defaultdict 
  
visited = defaultdict(lambda: False) 

# To store J1, J2 and Litre
J1, J2, L = 0, 0, 0
  
def Water_Jug_problem(X, Y):  
    
    global J1, J2, L
  
    if (X == L and Y == 0) or (Y == L and X == 0): 
        print("(",X, ", ",Y,")", sep ="") 
        return True
      
    if visited[(X, Y)] == False: 
        print("(",X, ", ",Y,")", sep ="") 
      
        visited[(X, Y)] = True
      
        return (Water_Jug_problem(0, Y) or
                Water_Jug_problem(X, 0) or
                Water_Jug_problem(J1, Y) or
                Water_Jug_problem(X, J2) or
                Water_Jug_problem(X + min(Y, (J1-X)), 
                Y - min(Y, (J1-X))) or
                Water_Jug_problem(X - min(X, (J2-Y)), 
                Y + min(X, (J2-Y)))) 
    else: 
        return False
  
# Main Code

J1 = 2 
J2 = 5 
L = 3
print("Path is as Follow:") 
  
Water_Jug_problem(0, 0)