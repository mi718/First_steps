# As you might know, it is not mathematically possible to divide a number by zero.
# Consequently, this is also not possible in Python either -you will get a ZeroDivisionError if you try:

#20 / 0

# With that in mind, your task for this exercise is to extend the program you created in Exercise
# 1 by displaying a message to the user when they enter 0 for the "total value".

try:
    total_value = float(input("total value: "))
    value = float(input("value: "))

    porcentaje = (100 / total_value) * value
    print(porcentaje)
except ValueError:
    print("You need to enter a number. Run the program again ")
except ZeroDivisionError:
    print("Your total value cannot be zero!!")