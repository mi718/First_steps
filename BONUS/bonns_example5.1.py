waitng_list = ["sen", "ben","john"]
waitng_list.sort()

for index, person in enumerate(waitng_list):
    row = f"{index +1}. {person.capitalize()}"
    print(row)