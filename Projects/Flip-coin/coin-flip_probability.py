while True:
    head_teal = input("Throw the coin and enter head or tail here: " + '\n') + '\n'

    with open("coin_side.txt" , 'r') as file:
        sides = file.readlines()

    sides.append(head_teal)

    with open("coin_side.txt" , 'w') as file:
        file.writelines(sides)

    nr_head = sides.count('head\n')
    percentage = nr_head / len(sides) * 100

    print(f'Heads {percentage}%')