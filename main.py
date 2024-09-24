# task manager
tasks = []

def add_task(task_name, *args, **kwargs):
    """
    Добавляет новую задачу в список задач.

    Параметры:
    - task_name (str): Название задачи
    - *args: Дополнительные неименованные параметры задачи (кортеж)
    - **kwargs: Дополнительные именованные параметры задачи (словарь)

    Функция создает задачу в виде словаря, содержащего информацию о:
    - 'name': название задачи
    - 'completed': статус выполнения (по умолчанию False)
    - 'additional': дополнительные параметры, переданные как *args
    - 'extra_info': дополнительные именованные параметры, переданные как **kwargs
    """
    task = {
        'name': task_name,  # Название задачи
        'completed': False,  # Статус выполнения задачи, по умолчанию False
        'additional': args,  # Дополнительные параметры сохраняются как кортеж
        'extra_info': kwargs  # Дополнительная информация сохраняется как словарь
    }
    tasks.append(task)  # Добавляем задачу в глобальный список tasks


# Примеры добавления задач
add_task('Buy food', place='Supermarket')
add_task('Write a report', department='HR', theme='Review')
add_task('Call a coworker', contact='Sergey')
add_task('Call a friend', contact='Anton')

# Выводим список задач для проверки
print(tasks)


def list_tasks(show_completed):
    """
    Выводит список задач с дополнительной информацией.

    Параметры:
    - show_completed (bool): Если True, выводит все задачи, включая завершенные.

    Для каждой задачи отображает:
    - порядковый номер задачи
    - название задачи
    - статус выполнения (завершено или в процессе)
    - дополнительную информацию в виде строки
    """
    print('\nList tasks: ')
    for index, task in enumerate(tasks):
        # Определяем статус задачи
        status = 'Completed' if task['completed'] else 'In the process'
        # Если задача завершена или флаг show_completed True, то отображаем задачу
        if not task['completed'] or show_completed:
            extra_info = []  # Список для хранения дополнительной информации
            for key, value in task['extra_info'].items():
                extra_info.append(f'{key}: {value}')  # Формируем строку для каждой пары ключ-значение
            extra_info_str = ', '.join(extra_info)  # Объединяем все пары ключ-значение в одну строку
            # Выводим задачу с порядковым номером, статусом и дополнительной информацией
            print(f'{index + 1}. {task["name"]} - {status} | {extra_info_str}')


# Выводим список всех задач (включая завершенные)
list_tasks(True)


def complete_task(task_index):
    """
    Помечает задачу как завершенную по её индексу.

    Параметры:
    - task_index (int): Порядковый номер задачи в списке (индексация начинается с 1 для удобства пользователя)
    """
    task = tasks[task_index - 1]  # Получаем задачу по индексу (индексация в списках начинается с 0)
    task['completed'] = True  # Помечаем задачу как завершенную
    print(f'\nTask {task["name"]} marked as complete')  # Выводим сообщение о завершении задачи


# Отмечаем 2-ю и 4-ю задачи как завершенные
complete_task(2)
complete_task(4)

# Выводим список незавершенных задач
list_tasks(True)# True = print all tasks, False = In the process only


def searching_task(keyword):
    """
    Ищет задачи по ключевому слову в названии задачи.

    Параметры:
    - keyword (str): Ключевое слово для поиска в названии задач

    Функция выводит найденные задачи с дополнительной информацией.
    """
    found = False  # Флаг, чтобы отслеживать, найдены ли задачи
    print(f'\nFound tasks: ')
    for task in tasks:
        # Если ключевое слово содержится в названии задачи (поиск регистронезависим)
        if keyword.lower() in task["name"].lower():
            extra_info = []  # Список для хранения дополнительной информации
            for key, value in task['extra_info'].items():
                extra_info.append(f'{key}: {value}')  # Формируем строку для каждой пары ключ-значение
            extra_info_str = ', '.join(extra_info)  # Объединяем все пары ключ-значение в строку
            print(f' - {task["name"]} | {extra_info_str}')  # Выводим найденную задачу с дополнительной информацией
            found = True  # Помечаем, что задачи были найдены
    if not found:
        print(f'No task were found')  # Если задачи не найдены, выводим сообщение


# Ищем задачи, содержащие слово 'call' в названии
searching_task('call')


def remove_completed_task(index=0):
    """
    Рекурсивно удаляет все завершенные задачи.

    Параметры:
    - index (int): Текущий индекс задачи для проверки (по умолчанию начинается с 0)

    Возвращает количество удаленных задач.
    """
    if index == len(tasks):
        return 0  # Базовый случай: если индекс равен длине списка, больше задач не осталось
    removed_count = 0  # Счетчик удаленных задач
    if tasks[index]['completed']:
        print(f'\nDeleting a completed task : {tasks[index]["name"]}')  # Выводим информацию об удалении задачи
        tasks.pop(index)  # Удаляем задачу из списка
        removed_count = 1  # Увеличиваем счетчик удаленных задач
        removed_count += remove_completed_task(index)  # Рекурсивно продолжаем проверку того же индекса
    else:
        removed_count += remove_completed_task(index + 1)  # Проверяем следующую задачу
    return removed_count  # Возвращаем общее количество удаленных задач


# Удаляем завершенные задачи
remove_completed_task()


# Пример рекурсии для вычисления суммы чисел
def sum_recursive(list_of_numbers):
    """
    Рекурсивно вычисляет сумму элементов списка.

    Параметры:
    - list_of_numbers (list): Список чисел

    Возвращает сумму всех элементов списка.
    """
    if len(list_of_numbers) == 0:
        return 0  # Базовый случай: если список пуст, возвращаем 0
    else:
        # Берем первый элемент списка и рекурсивно складываем его с суммой оставшихся элементов
        return list_of_numbers[0] + sum_recursive(list_of_numbers[1:])

# так выглядит стек вызовов в  sum_recursive
# 1 + [2, 3, 4, 5]
# 1 + 2 + [3, 4, 5]
# 1 + 2 + 3 + [4, 5]
# 1 + 2 + 3 + 4+ [5]
# 1 + 2 + 3 + 4 + 5
# if len(list_of_numbers) == 0:
# 0
# 15
#

# Список чисел для примера
list_ = [1, 2, 3, 4, 5]
# Вычисляем сумму элементов списка рекурсивно
res = sum_recursive(list_)
print(res)  # Выводим результат (должен быть 15)

