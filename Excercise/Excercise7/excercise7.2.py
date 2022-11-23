usernames = ["john 1990", "alberta1970", "magnola2000"]

# Extend the code above so the code prints out a list
# containing the number of characters for each username.

usernames = [len(username) for username in usernames]
print(usernames)
