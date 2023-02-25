def iterativeFactorial(num:int)->int: 
    f = 1
    for i in range(1, num +1): 
        f = f * i 
    return f


def recursionFactorial(n:int)->int:
    if (n==1 or n==0):
        return 1
    else:
        return (n * recursionFactorial(n - 1))
            

 
inputNum = [0, 5, 10, 25, 100]

print("Factorial results using an iterative Function")
for num in inputNum:
    print(str(num) + "! = " + str(iterativeFactorial(num)))

print("Factorial results using an recusion Function")
for num in inputNum:
    print(str(num) + "! = " + str(recursionFactorial(num)))



