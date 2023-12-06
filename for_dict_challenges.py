# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Петя"},
]


def count_students_name(students):
    dict_of_names_occurances = {}
    for student in students:
        name = student.get("first_name")
        if name in dict_of_names_occurances:
            dict_of_names_occurances[name] += 1
        else:
            dict_of_names_occurances[name] = 1
    for key, value in dict_of_names_occurances.items():
        print(f"{key}: {value}")


count_students_name(students)


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Оля"},
]


def most_common_name(students):
    dict_of_names_occurances = {}
    for student in students:
        name = student.get("first_name")
        if name in dict_of_names_occurances:
            dict_of_names_occurances[name] += 1
        else:
            dict_of_names_occurances[name] = 1

    common_name = max(dict_of_names_occurances, key=dict_of_names_occurances.get)

    print(f"Самое частое имя среди учеников: {common_name}")


most_common_name(students)

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {"first_name": "Вася"},
        {"first_name": "Вася"},
    ],
    [  # это – второй класс
        {"first_name": "Маша"},
        {"first_name": "Маша"},
        {"first_name": "Оля"},
    ],
    [  # это – третий класс
        {"first_name": "Женя"},
        {"first_name": "Петя"},
        {"first_name": "Женя"},
        {"first_name": "Саша"},
    ],
]


def common_name_in_class(school_students):
    for separate_class in school_students:
        dict_of_names_occurances = {}
        for student in separate_class:
            name = student.get("first_name")
            if name in dict_of_names_occurances:
                dict_of_names_occurances[name] += 1
            else:
                dict_of_names_occurances[name] = 1
        common_name = max(dict_of_names_occurances, key=dict_of_names_occurances.get)
        class_number = school_students.index(separate_class) + 1
        print(f"Самое частое имя в классе {class_number}: {common_name}")


common_name_in_class(school_students)


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "2б", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
    {
        "class": "2в",
        "students": [
            {"first_name": "Даша"},
            {"first_name": "Олег"},
            {"first_name": "Маша"},
        ],
    },
]
is_male = {
    "Олег": True,
    "Маша": False,
    "Оля": False,
    "Миша": True,
    "Даша": False,
}


def girls_and_boys(school, is_male):
    for index in range(len(school)):
        girls = 0
        boys = 0
        for student in school[index]["students"]:
            name = student["first_name"]
            if name in is_male:
                if not is_male[name]:
                    girls += 1
                else:
                    boys += 1
        print(f'в классе: {school[index]["class"]}: девочки {girls}, мальчики {boys}')


girls_and_boys(school, is_male)

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "3c", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
]
is_male = {
    "Маша": False,
    "Оля": False,
    "Олег": True,
    "Миша": True,
}


def gender_majority(school, is_male):
    dict_of_genders = {}
    for index in range(len(school)):
        girls = 0
        boys = 0
        class_name = school[index]["class"]
        for student in school[index]["students"]:
            name = student["first_name"]
            if name in is_male:
                if not is_male[name]:
                    girls += 1
                else:
                    boys += 1
        dict_of_genders[class_name] = {"девочки": girls, "мальчики": boys}
    print(dict_of_genders)

    # print(f'в классе: {school[index]["class"]}: девочки {girls}, мальчики {boys}')
    for class_name, gender_data in dict_of_genders.items():
        girls = gender_data["девочки"]
        boys = gender_data["мальчики"]
        if girls > boys:
            print(f"Больше всего девочек в классе {class_name}")
        elif boys > girls:
            print(f"Больше всего мальчиков в классе {class_name}")
        else:
            print(f"в классах одинаковое количество девочек и мальчиков")


gender_majority(school, is_male)
