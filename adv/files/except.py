x = int(input("x: "))
y = int(input("y: "))

try:
    print("x / y =",x/y)
except ZeroDivisionError:
    print("ZeroDivisionError:")
    y = int(input("y: "))

print("x / y =", x / y)

print("End")
