# This program will calculate the factorial of a non-negative number

#completion: i defined both functions (factorial, checkpos), then implemented the conditionals
#            used to check if the number was either positive, or to implement a factorial function.


def checkPositive(n):
    if n > 0:
        return True
    else:
        return False

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


#main body of the program

terminate = False

while not terminate:
    n = int(input("enter a number greater than 0 : "))
    while not checkPositive(n):
        print("You need to enter a number greater than 0")
        n = int(input("enter a number greater than 0 : "))
    f = factorial(n)
    print ("The factorial of ",n,"is ", f)
    answer = input("Do you want to play again (y/n): ")
    if answer.lower() == 'y':
        terminate = False
    else:
        terminate = True
