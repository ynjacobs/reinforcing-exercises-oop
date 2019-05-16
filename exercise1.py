class Task:

    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return 'the task is to {} by {}'.format(self.description, self.due_date)

    def __repr__(self):
        return 'the task is to {} by {}'.format(self.description, self.due_date)


plant_flowers = Task('plant and water flowers', 'May 20')
print(plant_flowers)

buy_milk = Task('buy milk from store', 'May 22')
print(buy_milk)

buy_new_phone = Task('buy a new Samsung', 'May 21')
print(buy_new_phone)
    