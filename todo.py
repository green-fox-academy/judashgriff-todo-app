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
                self.check_items(todo_list)    


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
        todo_list = []
        with open('todo.txt', 'r') as text:
            for line in text:
                d = {}
                checked_line = self.if_checked(line)
                d["text"] = line
                d["check"] = checked_line    
                todo_list.append(d)
        return todo_list

    def if_checked(self, line):
        if line[0] != 0 and line[0] != 1:
            checking = 0 
            return checking
        else:
            return line

    def list_items(self, todo_list):
        if todo_list == []:
            print('No todos for today! :)')
        else:
            for i, task in enumerate(todo_list):
                if task['check'] == 0:
                    print(str(i + 1) + " - [ ]" + task['text'])
                if task['check'] == 1:
                    print(str(i + 1)+ " - [x]" + task['text'])

    def add_items(self, todo_list):
        with open('todo.txt', 'a') as text:
            new_task = input('What do you want to add to the list? \n')
            text.write(new_task + '\n')
        return self.new_list()
        
    def new_list(self):
        print('\nThe list is the following now: \n')
        todo_list = self.make_dictionary()
        return self.list_items(todo_list)
        

    def remove_items(self, todo_list):
        pass


    def check_items(self, todo_list):
        pass


      

screen = Controller()