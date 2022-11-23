import glob

gen = glob.glob("Excercise6/*.txt")

for i in gen:
    with open(i, 'r') as file:
        print(file.read().upper())