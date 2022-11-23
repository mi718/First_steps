from fun import get_todos, write_todos
import time

def loop():
    date_function = time.strftime("%B %d, %Y %H:%M:%S")
    print(f"It is {date_function}")
    while True:
        # Get user input, strip space chars and uppercase words from it
        user_prompt = "type 'add', 'show','edit','count','complete', 'clear' or 'exit': "
        user_action = input(user_prompt).lower() + '\n'
        user_action = user_action.strip()

        if user_action.startswith("add"):
            todo = user_action[4:]

            todos = get_todos()

            todos.append(todo + '\n')

            write_todos(todos)

        elif user_action.startswith("show"):

            todos = get_todos()

            for index, objects in enumerate(todos):
                objects = objects.strip('\n')
                print(f"{index +1}- {objects}")

            if len(todos) == 0:
                print("THE TO-DO LIST IS EMPTY")


        elif user_action.startswith("edit"):
            try:
                number = int(user_action[5:])
                number = number - 1

                todos = get_todos()

                for index, objects in enumerate(todos):
                    objects = objects.strip('\n')
                    print(f"{index +1}- {objects}")

                new_todo = input("ENTER NEW TO-DO: ").title()
                todos[number] = new_todo

                for index, objects in enumerate(todos):
                    objects = objects.strip('\n')
                    print(f"{index+1}- {objects}")

                write_todos(todos)

            except:
                print("You command is not valid. Try typing edit + number of the todo to edit and press ENTER")
                continue

        elif user_action.startswith("complete"):
            try:
                todos = get_todos()

                listo = 'TASK COMPLETE'

                for index, objects in enumerate(todos):
                    objects = objects.strip('\n')
                    print(f"{index+1}- {objects}")
                what = int(user_action[9:])
                what = what - 1
                competed = todos.pop(what)
                print("GREAT WORK!!! KEEP WORKING.")
                for index, objects in enumerate(todos):
                    objects = objects.strip('\n')
                    print(f"{index +1}- {objects}")

                write_todos(todos)

                with open('completed_task.txt', "r") as finish_file:
                    end = finish_file.readlines()

                end.append(competed)

                with  open('completed_task.txt', "w") as finish_file:
                    finish_file.writelines(end)
            except:
                print("You command is not valid. Try typing complete + number of the completed task and press ENTER")
                continue

        elif user_action.startswith("count"):

            todos = get_todos()

            print(f"YOUR TO-LIST HAS {len(todos)} ITEMS")
        elif user_action.startswith("clear"):

            todos = get_todos()

            todos.clear()
            print("TO-DO LIST IS EMPTY")

            write_todos( todos)

        elif user_action.startswith("exit"):
            break

        else:
            print("//// HEY, YOU ENTER AN UNKNOW COMMAND //// TRY AGAIN ----->")
    return ""

    print("///TO-DO LIST IS COMPLETED///")


while True:
    ope = input("OPEN TODO LIST? 'YES' / 'N0': ").lower()
    match ope:
        case 'yes':
            print(loop())
            continue
        case 'no':
            print("SEE YOU NEXT TIME")
            break