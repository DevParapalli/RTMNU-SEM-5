state=[0,0]
def Update(count,X,Y,flag):
    state[0]=X
    state[1]=Y
    if flag :
        print(state)
    
    count=count+1
    return count



def Jug(Xmax,Ymax,d,flag):
    count=0
    X=Xmax
    Y=0

    count=Update(count,X,Y,flag)
    while state[0]!=d and state[1]!=d :
        temp=min(X,Ymax-Y)
        Y=Y+temp
        X=X-temp
        count=Update(count,X,Y,flag)
        if (state[0] == d or state[1] == d):
            break

        if X==0 :
            X=Xmax
            count=Update(count,X,Y,flag)
    
        if Y==Ymax :
            Y=0
            count=Update(count,X,Y,flag)
    
        
    return count



x=int( input("enter the capacity of larger jug: "))
y=int( input("enter the capacity of smaller jug: "))
d=int( input("Enter the amount of water required: "))
count1=Jug(x,y,d,0)
count2=Jug(y,x,d,0)

if count1<=count2:
    Jug(x,y,d,1)
    print("Number of steps reuired :"+str(count1))
else:
    Jug(y,x,d,1)
    print("Number of steps reuired :"+str(count2))