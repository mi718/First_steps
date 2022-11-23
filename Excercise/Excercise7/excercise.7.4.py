user_entries = ['10', '19.1', '20']

# Extend the code above so the code prints out the sum of the numbers.

user_entries = [float(user_entry) for user_entry in user_entries]
print(sum(user_entries))
