user_entries = ['10', '19.1', '20']

# Extend the code above so the code prints out a list containing the same items as floats.

user_entries = [float(user_entry) for user_entry in user_entries]
print(user_entries)