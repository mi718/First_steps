# same as excercise 12.2.py

'''print("This is a passwors strengh tester.")
password = input("Enter your Passwor: ")

result = {}

if len(password) >= 9:
    result["lenght"] = True
else:
    result["lenght"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

cap = False
for x in password:
    if x.isupper():
        cap = True
result["upper-or-lower"] = cap

print(result)

if all(result.values()) == True:
    print("Strong Password")
else:
    print("Weak Password")'''''