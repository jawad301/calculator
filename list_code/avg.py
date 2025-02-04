number = [3, 8, 15, 23, 42]
number_enter = int (input("Enter the number :"))
average = sum(number)/len(number)
if number_enter > average:
    print("The number is greater than average")
else :
    print("The number is less than average")