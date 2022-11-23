# Write a program that asks users to enter a password. Then, it checks if the password
# length is greater than 7 and returns "Great password there!".

# If the password has 7 or fewer characters, the program returns "Your password is weak".

password = input("Enter your password:")

if len(password) >  7:
    print("Great password there!!!")
elif len(password) == 7:
    print("Password is OK, but not to strong")
elif len(password) < 7:
    print("Your password is weak!!!")