from task import Task

# task1 = Task('ivan','2024-02-20') # получаем ошибку по формату даты '20-02-2024'
task1 = Task('ivan', '20-02-2024')
print(task1)  # магический метод
print(task1.show_info())  # через show

