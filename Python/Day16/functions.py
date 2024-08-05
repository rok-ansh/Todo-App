
FILEPATH = 'todos_item.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as filepath_local:
        todos_local = filepath_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as filepath_local:
        filepath_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())



