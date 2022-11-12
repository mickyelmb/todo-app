FILEPATH = "text_files/todos.txt"
def get_todos(filepath=FILEPATH):
    """
    Read a to-do files from todos.txt
    :param filepath:
    :return: list of file data
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos( todos_args, filepath=FILEPATH):
    """
    Write new or edited items to the todos.txt file
    :param todos_args:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos_args)

#print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())