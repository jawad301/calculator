def celsius_to_fahrenheit (celsius) :
    fahrenheit = (celsius * 9/5) + 32
    print ("Temperature in fahrenheit is " , fahrenheit)
user =  int (input("Enter temperature in celsius : "))
celsius_to_fahrenheit(user)