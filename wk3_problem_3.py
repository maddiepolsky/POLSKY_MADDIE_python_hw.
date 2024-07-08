#Write a recursive function factorial(n) that returns the factorial of a given number.
def factorial (n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print (factorial(5))
print (factorial(1))
print (factorial(100))
print (factorial(10))
print (factorial(4))
