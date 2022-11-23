filenames = ['document', 'report', 'presentation']

for index, name in enumerate(filenames):
    extend = f"{index +1}-{name.capitalize()}.txt"
    print(extend)