   # Please download the three text files a.txt, b.txt, and c.txt from the resources.
# Then, create a program that reads each text file and prints out the content of
# each in the command line. The expected output would be like the following:

file_names = ['a.txt', 'b.txt', 'c.txt' ]

for file_name in file_names:
    file = open(file_name, 'r')
    content = file.read()
    print(content)