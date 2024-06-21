# """
# зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку
# здійснюється за механізмом
# student[outer_dict_key][inner_dict_key]
#
# Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
# 1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення,
#     бал від 0 до 100 (інт чи флоат)
# 2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
#     сам формат наповнення цього списку up to you
# 3 - визначити середній бал по групі
# 4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)
#
# не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
# """
students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
# ваш код нижче !!!!!!!! вище нічого не змінюємо

from pywebio.output import put_text, put_html, put_error
from pywebio import start_server

# add a new student
students['Мірошніченко Вікторія'] = {
    'Пошта': 'vika24358@gmail.com',
    'Вік': 18,
    'Номер телефону': '+380980073355',
    'Середній бал': 100}


# create and display list with students, whose average grade is above 90
def get_students_with_high_grade(students_list):
    high_grade_students_list = []
    for student, features in students_list.items():
        if features['Середній бал'] > 90:
            high_grade_students_list.append({student: features['Середній бал']})
            put_text(f"{student}: Середній бал - {features['Середній бал']}")
    return high_grade_students_list


# calculate average grade
def get_average_grade(students_list):
    total_grade = 0
    student_number = 0
    for details in students_list.values():
        total_grade += details['Середній бал']
        student_number += 1
    if student_number:
        average_grade = total_grade / student_number
    else:
        put_error('У вашому списку не було знайдено жодного студента(')
        average_grade = None
    return average_grade


def main():
    # identify and display students with average grade above 90
    put_html("<h2>Студенти з середнім балом більше 90:</h2>")
    high_grade_students = get_students_with_high_grade(students)

    # replace phone number where not given
    for student, features in students.items():
        if features["Номер телефону"] is None:
            features["Номер телефону"] = '+3801112233'

    # calculate and display average grade
    average_grade_in_group = get_average_grade(students)
    if average_grade_in_group is not None:
        put_html(f"<h3>Середній бал усієї групи: {average_grade_in_group} </h3>")


if __name__ == '__main__':
    start_server(main, port=15000)
