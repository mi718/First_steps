# This time you need to create a program that:
    # 1. Contains the above list.
    # 2 Prompts the user to input the person's name.
    # 3. Returns the rank that person has.


ranking = ["Jim", "Manuel", "Isabela"]

rankperson = input("ENTER PERSON NAME: ").lower()

match rankperson    :
    case "jim":
        print(ranking[0] +1)
    case "manuel":
        print(ranking[1] +1)
    case "isabel":
        print(ranking[2] +1)
    case '_':
        print("////PERSON IS NOT IN THE LIST////")

