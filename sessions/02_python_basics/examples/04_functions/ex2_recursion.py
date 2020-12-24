# recursion
def Fibonacci(iteration): 
    if iteration<=0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif iteration==1: 
        return 0
    # Second Fibonacci number is 1 
    elif iteration==2: 
        return 1
    else:
        #print(iteration)
        return Fibonacci(iteration-1)+Fibonacci(iteration-2) 

iteration = 10
for i in range(iteration):
    print(Fibonacci(i)) 