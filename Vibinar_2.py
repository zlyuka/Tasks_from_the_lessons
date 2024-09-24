# Картотека сотрудников (список сотрудников)
employees = [
    {"name": "Валерий", "position": "Менеджер", "department": "Продажи"},
    {"name": "Олег", "position": "Менеджер", "department": "Продажи"},
    {"name": "Ольга", "position": "Разработчик", "department": "ИТ"},
    {"name": "Владислав", "position": "Менеджер", "department": "Продажи"},
    {"name": "ВлаДимир", "position": "Разработчик", "department": "ИТ"},
    {"name": "Анна", "position": "Бухгалтер", "department": "Финансы"},
]


def find_name(name):
    '''Функция для поиска сотрудника в картотеке'''
    for emp in employees:
        if emp["name"].lower() == name.lower():
            return emp
    return None


def filtred_emp(position):
    '''Функци фильтрует по должности и распечатывает сотрудника '''
    filter_emp = []
    for emp in employees:
        if emp["position"].lower() == position.lower():
            filter_emp.append(emp)
    return filter_emp


def add_emp(name, position, department):
    '''Добавление нового сотрудника'''
    employees_extend = {"name": 1 , "position": 1, "department": 1}
    employees_extend["name"] = name
    employees_extend["position"] = position
    employees_extend["department"] = department
    print('Новый сотрудник добавлен')
    return employees_extend








def main():
    while True:
        print(f'\nMenu')
        print(f'1. поиск сотрудника по имени')
        print(f'2. фильтровать сотрудников по должности')
        print(f'3. добавить нового сотрудника')
        print(f'4. выход из программы')
        choice = input('Введите  пункт меню: ')

        if choice == '1':
            name = input('Введите имя сотрудника:')
            employee = find_name(name)
            if employee:
                print(f'Сотрудник {employee["name"]}\n'
                      f'Должность {employee["position"]}\n'
                      f'работает в отделе {employee["department"]}')
            else:
                print('Сотрудник не найден')

        elif choice == '2':
            position = input('Введите должность ')
            filtered_emp = filtred_emp(position)
            if filtered_emp:
                print('\nСотрудники с данной должностью:')
                for emp in filtered_emp:
                    print(f'Имя {emp["name"]} Отдел {emp["department"]}')
            else:
                print(f'Сотрудников с такой должностью нет')

        elif choice == '3':
            name = input('Введите имя нового сотрудника ')
            position = input('Введите должность нового сотрудника сотрудника ')
            department = input('Введите отдел нового сотрудника ')
            employees_extend = add_emp(name, position, department)
            employees.append(employees_extend)
            print( )

        elif choice == '4':
            print('EXIT')
            break


if __name__ == "__main__":
    main()
