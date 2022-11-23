liters = float(input("Enter the amount of liters you whish to convert into cubic meters: "))

def liter_function(how_much):
    cubic_meters = how_much / 1000
    return cubic_meters

print(f"{liters} liters in m^3: {liter_function(liters)}m^3")