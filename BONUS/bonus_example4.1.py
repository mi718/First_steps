filenames = ["1- Micael - Staubli" , "2- Andres - Gonazales"]

for filename in filenames:
    filename = filename.replace("-" , ".", 1)
    print(filename)