todos=[]
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    todos.append(title)
    print("1 task added")
    print_list()
    

def print_list():
    global todos
    print(todos)

def delete_task(number_to_delete):
    del todos[int(number_to_delete)]
    print_list()

def save_todos():
    with open("todos_file.csv", "w+" ) as f:
        f.write(",".join(todos))
    print("New task is saved")

    
def load_todos():
    with open("todos_file.csv", "r" ) as f:
        jr = f.readline()
    print(jr)

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")