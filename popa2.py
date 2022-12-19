import tabulate # Импорт табурета


# Страница челабобусов
def spisok():
    print(" Список всех сотрудников:")
    from tabulate import tabulate
    data = []
    with open('list.txt',encoding="utf-8") as f: #открытие файла и добавление формата
        for line in f:
            data.append(list(map(str.strip, line.split(',')))) #сама табуретка
    print(tabulate(data, tablefmt='grid', headers=('Фамилия', 'Год рождения', 'Должность', 'Стаж', 'Образование'))) #формат и что будет написано
    avg()

#Считает среднее значение
def avg():
    with open('list.txt',encoding="utf-8") as f:
        total = 0
        count = 0
        for line in f:
            field1, field2, field3, field4, field5 = line.split(',')
            total += int(field4)
            count += 1
    result = total / count
    print("Средний стаж всех работников:")
    print(result)


#Добавить  чела
#Name - имя, Year - год рождения, Pos - должность, Exp - стаж, Образование - Edu
def add(Name=None, Year=None, Pos=None, Exp=None, Edu=None):
    Name = input("Введи фамилию сотрудника:")
    Year = input("Введи год рождения сотрудника:")
    Pos = input("Введи должность сотрудника:")
    Exp = input("Введи стаж сотрудника")
    Edu = input("Введи образование сотрудника:")
    list = open("list.txt", "a", encoding="utf-8")                       # Открывает список  и ставит кадировку
    list.write(Name+", "+str(Year)+ ", "+str(Pos)+", "+str(Exp)+ ", "+str(Edu)+"\n")     #записывает  в файл
    print("Сотрудник добавлен!")
    list.close()                              #сохраняет и закрывает
    home()                                # кидает обратно

#страница удаления рабов
def remove(Name1=None, Year2=None):
    spisok()
    Name1 = input ("Напиши фамилию сотрудника, которого бы хотел уволить:")
    Year2 = input ("А теперь напиши его год рождения:")
    fn = 'list.txt'   #открывает лист
    f = open(fn, encoding="utf-8")
    output = []
    for line in f:
        if not (Name1 and Year2) in line:
            output.append(line)
    f.close()
    f = open(fn, 'w', encoding="utf-8")
    f.writelines(output)
    f.close()
    print('''Ты его уволил, ты настоящий БОСС! Возвращение на главную страницу...
    ---
    
    ---''')
    home()

#Сортировка
def sort():
    from tabulate import tabulate
    data = []
    with open('list.txt',encoding="utf-8") as f:
        for line in f:
            if 'Мастер' in line and 'Вышка' in line.split():
                data.append(list(map(str.strip, line.split(',')))) #сама табуретка
    print(tabulate(data, tablefmt='grid', headers=('Фамилия', 'Год рождения', 'Должность', 'Стаж', 'Образование'))) #формат и что будет написано
    with open('list.txt',encoding="utf-8") as f:
        total = 0
        count = 0
        for line in f:
            if 'Мастер' in line and 'Вышка' in line.split():
                field1, field2, field3, field4, field5 = line.split(',')
                total += int(field4)
                count += 1
    result = total / count
    print("Средний стаж мастеров с высшем образованием:")
    print(result)

def home(): # Главная страница
    print('''Выберите пункт меню:
    1. Показать всех сотрудников
    2. Добавить сотрудника
    3. Уволить сотрудника
    4. Отсортировать сотрудников с высшем образованием''')
    user_input = input()
    if user_input == '1':
        spisok()
    elif user_input == '2':
        add()
    elif user_input == '3':
        remove()
    elif user_input == '4':
        sort()
    else:
        print("Ты что-то не так написал")
home()
