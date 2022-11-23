# Build a percentage calculator that gets from the user the "total value"
# and the "value" and returns the percentage as shown below:

# The program should also print a message if the user doesn't
# enter a number for the "total value or for the "value":


try:
    total_value = float(input("total value: "))
    value = float(input("value: "))

    porcentaje = (100 / total_value) * value
    print(porcentaje)
except ValueError:
    print("You need to enter a number. Run the program again ")