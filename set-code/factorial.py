def find_factorial (num) : 
    return 1 if num == 0 else num * find_factorial(num - 1) 
user = int(input("Enter a number: "))
result = find_factorial(user)
print ( "The factorial of the Number is:",result)
