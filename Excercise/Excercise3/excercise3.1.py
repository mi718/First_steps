# Write a program that asks the user to enter the country they are from.
# If the user enters USA, the program prints out Hello. If the user enters
# the word  India, the program prints out Namaste. If the user enters the word Germany,
# the program prints out Hallo.

country_name = "Enter you country: "

while True:
    deciosion = input(country_name).lower()
    deciosion = deciosion.strip()
    match deciosion:
        case "usa":
            print("Hello")
        case "germany":
            print("Hallo")
        case "india":
            print("Namaste")
        case _:
            print("//// HEY!!! YOU ENTER AN UNKNOWN COMMAND //// TRY AGAIN -----> ")

print("THANKS :)")