# Please download the members.txt file from the resources of this article.
# Then, create a program that, whenever executed, asks the user to enter a
# new member in the command line:

user = input('Enter a new member to the list: ')

file = open('members.txt', 'r')
content = file.readlines()
file.close()

content.append(user + "\n")
for i,names in enumerate(content):
    print(i, names)


file = open('members.txt', 'w')
file.writelines(content)
file.close()