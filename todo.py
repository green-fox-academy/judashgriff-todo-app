from sys import argv

class Controller(object):
    def __init__(self):
        if len(argv) == 1:
            self.lets_print()
        else:
            todo_list = self.make_dictionary()
            if argv[1] == '-l':
                self.list_items(todo_list)
            elif argv[1] == '-a':
                self.add_items(todo_list)
            elif argv[1] == '-r':
                self.remove_items(todo_list)
            elif argv[1] == '-c':
                self.switch_check(todo_list)    


    def lets_print(self):
        print(str("\n\
        Command Line Todo application\n\
        =============================\n\n\
        Command line arguments:\n\
         -l   Lists all the tasks\n\
         -a   Adds a new task in following method: -a \"your text\"\n\
         -r   Removes a task in following method: -r \"task to remove\"\n\
         -c   Completes an task in following method: -c \"task to comply\""))

    def make_dictionary(self):
        todo_list = []
        with open('todo.txt', 'r') as text:
            for line in text:
                d = {}
                checked_line = self.check_items(line)
                d["text"] = line
                d["check"] = checked_line    
                todo_list.append(d)
        return todo_list

    def check_items(self, line):
        if line[0] != 0 and line[0] != 1:
            checking = 0 
            return checking
        else:
            return line

    def switch_check(self, todo_list):
        if len(argv) < 3 or len(argv) > 3:
            self.lets_print()
        elif len(argv) == 3:
            to_switch = argv[2]
            for i, line in enumerate(todo_list):
                    if to_switch == todo_list[i]['text']:
                        if todo_list[i]['check'] == 1:
                            todo_list[i]['check'] = 0
                        elif todo_list[i]['check'] == 0:
                            todo_list[i]['check'] = 1
            self.list_items(todo_list)

    def list_items(self, todo_list):
        if todo_list == []:
            print('\nNo todos for today! :)')
        else:
            print('\n')
            for i, task in enumerate(todo_list):
                if task['check'] == 0:
                    print(str(i + 1) + " - [ ]" + task['text'])
                else task['check'] == 1:
                    print(str(i + 1)+ " - [x]" + task['text'])

    def add_items(self, todo_list):
        if len(argv) < 3 or len(argv) > 3:
            self.lets_print()
        else:
            with open('todo.txt', 'a') as text:
                new_task = argv[2]
                text.write(new_task + '\n')
            self.new_list()
        
    def new_list(self):
        print('\nThe list is the following now: \n')
        todo_list = self.make_dictionary()
        return self.list_items(todo_list)

    def remove_items(self, todo_list):
        if len(argv) < 3 or len(argv) > 3:
            self.lets_print()
        elif len(argv) == 3:
            to_remove = argv[2]
            with open('todo.txt', 'w') as text:
                for i, line in enumerate(todo_list):
                    if to_remove == todo_list[i]['text']:
                        todo_list -= todo_list[i]
            self.new_list()


      

screen = Controller()