x = ("applle","banana","orange")
y = list(x)
y[0] = "kiwi"
x = tuple(y)
print(type(y))
print(x)