from sys import argv

class Controller(object):
    def __init__(self):
        if len(argv) == 1:
            self.lets_print()
        else:
            self.todo_dict = self.make_dictionary()
            if argv[1] == '-l':
                self.list_items()
            elif argv[1] == '-a':
                self.add_items()
            elif argv[1] == '-r':
                self.remove_items()
            elif argv[1] == '-c':
                self.check_items()    

    def lets_print(self):
        print(str("\n\
        Command Line Todo application\n\
        =============================\n\n\
        Command line arguments:\n\
         -l   Lists all the tasks\n\
         -a   Adds a new task\n\
         -r   Removes a task\n\
         -c   Completes an task"))

    def make_dictionary(self):
        todo_dict = []
        current_line = 1
        with open('todo.txt', 'r') as text
        for line in text:
            d = {}
            todo_dict[line] = line
            todo_dict.append(d)
        print(todo_dict)
        return todo_dict

todo_dict = [
    {"line_num": 1, "todo": 'buy milk'}
]

    def list_items(self):
        with open('todo.txt', 'r') as text
        current_line = 1
        for line in text:
            print(str(current_line) + ". " + line)
            current_line += 1

    def add_items(self):
        with open('todo.txt', 'a') as text
        text.write(input('What do you want to add to the list?\n'))
        print('\nThe list is the following now: ')
        self.list_items()

    def remove_items(self):
        pass


    def check_items(self):
        pass



        


screen = Controller()