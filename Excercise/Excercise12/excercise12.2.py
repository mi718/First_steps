# Create a script that asks the user to enter a password. Then create a
# function that checks the strength of the user password. The function should
# return Strong Password if all of the following conditions are true:

password = input("Enter your password please: ")

# Eight or more characters
# At least one uppercase letter.
# At least one digit.

def strength(pas):

    result = {}
    if len(pas) >= 9:
        result["lenght"] = True
    else:
        result["lenght"] = False

    digit = False

    for i in pas:
        if i.isdigit():
            digit = True
    result["digit"] = digit

    cap = False

    for x in pas:
        if x.isupper():
            cap = True
    result["upper-or-lower"] = cap

    print(result)

    if all(result.values()) == True:
        print("Strong Password")
    else:
        print("Weak Password")

    return "Bye"
print(strength(password))