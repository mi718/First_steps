# Extend the program you wrote in exercise 2 by printing a message to the user instead
# of their age if their age is greater than 120. Feel free to print any message that you lik

''''def age(year_of_birth, current_year = 2022):
    old = current_year - year_of_birth
    return old

user_age = int(input("What is your year of birth? "))

print(age(user_age))'''''

def age(year_of_birth, current_year = 2022):
    old = current_year - year_of_birth
    return old

user_age = int(input("What is your year of birth? "))

total_age = (age(user_age))

if total_age > 120:
    print("WOW you are old !!!")
elif total_age < 120:
    print(f"You are {total_age} years old")
