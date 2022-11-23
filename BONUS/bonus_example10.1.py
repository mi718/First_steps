try:
    length = float(input("high of your rectangle: "))
    width = float(input("widht of your rectangle: "))

    if length == width or width == length:
        exit("UPS!!! That looks like a square")

    diameter = length * width
    print(f"Your rectangle diameter is {diameter}")
except ValueError:
    print("UPS!!! Try with a number")