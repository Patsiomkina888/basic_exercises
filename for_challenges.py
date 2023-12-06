# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ["Оля", "Петя", "Вася", "Маша"]


def show_names(list_of_names):
    for name in list_of_names:
        print(name)
    return "Имена закончились"


show_names(names)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ["Оля", "Петя", "Вася", "Маша"]


def show_names_and_chars(list_of_names):
    for name in list_of_names:
        print(f"{name}: {len(name)}")
    return "Имена закончились"


show_names_and_chars(names)


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    "Оля": False,  # если False, то пол женский
    "Петя": True,  # если True, то пол мужской
    "Вася": True,
    "Маша": False,
}
names = ["Оля", "Петя", "Вася", "Маша"]


def show_names_and_gender(list_of_names):
    for name in list_of_names:
        if not is_male.get(name, False):
            print(f"{name}: женский")
        else:
            print(f"{name}: мужской")
    return "Конец списка"


show_names_and_gender(names)


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ["Вася", "Маша"],
    ["Вася", "Маша", "Саша", "Женя"],
    ["Оля", "Петя", "Гриша"],
]


def number_of_students(groups):
    number_of_groups = len(groups)
    print(f"Всего {number_of_groups} групп(a/ы)")
    for number, group in enumerate(groups, start=1):
        print(f"Группа {number}: {len(group)} ученика(-ов)")
    return "Конец списка"


number_of_students(groups)

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ["Вася", "Маша"],
    ["Оля", "Петя", "Гриша"],
    ["Вася", "Маша", "Саша", "Женя"],
]


def list_of_students(groups):
    number = 1
    for group in groups:
        print(f"Группа {number}: {', '.join(group)}")
        # for name in group:
        #     print(name)

        number += 1
    return "Конец списка"


list_of_students(groups)
