file_names = ['members.txt', 'essay.txt', 'presentation.txt']

for names in file_names:
    file = open(names, 'w')
    file.write('Hello')
    file.close()