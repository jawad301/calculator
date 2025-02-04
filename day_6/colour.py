colour = ["red", "green", "blue", "yellow", "purple"]
colour_name = input ("Enter a colour name: ")
if colour_name in colour:
    colour_to_remove = "colour"
    colour.remove(colour_name)
    print("The updated list is: ", colour)
else:
    print("Colour not found in the list")