from exercise1 import *

class TodoList:

    

    def __init__(self, name):
        self.name = name
        self.tasks_list = []


    def __str__(self):
        messages = f'{self.name}: \n'
        for task in self.tasks_list:
            messages += ' ' + task.description + '\n'
        return messages

    
    def add_task(self, pass_task):
        self.tasks_list.append(pass_task)
    
first_todo = TodoList('first to do')
first_todo.add_task(plant_flowers)
first_todo.add_task(buy_milk)
first_todo.add_task(buy_new_phone)
print(first_todo)
print(first_todo.tasks_list)
