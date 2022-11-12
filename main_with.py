"""
Creates, Edits and Removes items from a to-do list.
test
"""

import time
from functions import get_todos, write_todos
now = time.strftime("%b/%d/%Y %H %M %A AM")
print("The date and time is now", now)
Print("Git Test")
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        # new_todos = []
        # for item in todos:  * Does the same thing as list comprehension on line 23
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = user_action[5:]
            number = int(number) - 1
            todos = get_todos()
            new_todo = input("Enter the new todo item: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is invalid. Please use the number of the list.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo item {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("The item is not in the list of todos")
            continue
    elif 'exit' in user_action:
        print("Get to work!")
        break
    else:
        print("The command is invalid")



