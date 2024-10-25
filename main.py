def towerofhanoi(n,A,B,C):
    if n ==1:
        move(A,C)
    else:
        towerofhanoi(n-1,A,C,B)
        move(A,C)
        towerofhanoi(n-1,B,A,C)
def move(X,Y):
    print("move", X, "to", Y)

n =int(input("inter the number of dicks"))
towerofhanoi(n,"A","B","C")    
