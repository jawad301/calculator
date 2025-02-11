# def greet_user(name):
#     print("Hello, " + name + "! Welcome!")

# # Take input outside the function
# user_name = input("Enter your name: ")

# # Call the function with the user input
# greet_user(user_name)


# def square_number(num):
#     print ("The square of the number is: ", num ** 2)
    
# user_num =  int(input("Enter your desired num:"))

# square_number(user_num)


# def check_even_odd (num):
#     if num % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")
# user_num = int(input("Enter your number:"))
# check_even_odd(user_num)


# def find_max(num1,num2):
#     if num1 > num2:
#         print("The first number is greater")
#     elif num1 < num2 :
#         print ("The second number is greater")
#     elif num1 == num2 :
#         print ("Both number are same")
        
# user_num1= int (input("Enter your desirde Number:"))
# user_num2 = int(input("Enter your second number:"))
# find_max(user_num1,user_num2)


def calculate_area (length , width):
    area = length * width
    print("The area of the rectangle is: ", area)
user_length = int (input("Enter the length :"))
user_width = int (input("Enter the width :"))
calculate_area(user_length,user_width)  # calling the function with user input