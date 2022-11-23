# Your task for this exercise is to use the function you created in exercise 1.


'''def age(year_of_birth, current_year = 2022):
    old = current_year - year_of_birth
    return old

print(age(2004))'''

# Then, below the function definition, get the year of birth from the user using
# an input function and then call and print the defined function to get the user's
# age as output. Here is how the program should behave:

def age(year_of_birth, current_year = 2022):
    old = current_year - year_of_birth
    return old

user_age = int(input("What is your year of birth? "))

print(age(user_age))
