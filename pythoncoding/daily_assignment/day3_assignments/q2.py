#factorial using user-defined function
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print("factorial of 5:",factorial(5))