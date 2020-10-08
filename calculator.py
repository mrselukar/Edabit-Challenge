x = float(input ("enter first number: "))
a = input ("enter operation:")
y = float(input ("enter second number: "))
if a == "+":
    result = (x+y)
if a == "-":
    result = (x-y)
if a == "*":
    result = (x*y)
if a == "/":
    result = (x/y)
print(result)