# The function we wrote in exercise 1 returned 9.7.
# Change the function so this time it returns Max: 9.7, Min: 9.2 where 9.7 is the maximum and 9.2 is the minimum.

def get_max():
    grades = [9.6, 9.2, 9.7]
    min_grades = min(grades)
    max_grades = max(grades)
    message = f"Max: {max_grades}, Min: {min_grades}"
    return message

print(get_max())
