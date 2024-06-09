from pywebio.input import input as input_pw
from pywebio.input import NUMBER, TEXT
from pywebio.output import put_html, put_image
from pywebio import start_server
from pywebio.session import run_js

total_score = 0

MSG_GREETING_TEXT = "Вітаємо у нашій вікторині! Як вас звати?"

# questions list
MSG_QUESTION_01 = "Як називається трикутник, у якого всі сторони та кути рівні між собою?"
MSG_QUESTION_02 = "Яка сума всіх кутів чотирикутника?"
MSG_QUESTION_03 = "Як називається найдовша сторона прямокутного трикутника?"
MSG_QUESTION_04 = "Яка фігура має 8 сторін?"
MSG_QUESTION_05 = "Яке число є коренем квадратним числа 144?"

# answers list
MSG_ANSWER_01 = "рівносторонній"
MSG_ANSWER_02 = 360
MSG_ANSWER_03 = "гіпотенуза"
MSG_ANSWER_04 = "октагон"
MSG_ANSWER_05 = 12


def ask_and_format_user_name(greeting_text: str) -> str:
    username = input_pw(greeting_text)
    formatted_user_name = str(username).strip().title()
    return formatted_user_name


def get_user_answer_template_str(question: str) -> str:
    user_answer = input_pw(f'{question}', type=TEXT)
    formatted_user_answer = str(user_answer).lower().strip()
    return formatted_user_answer


def get_user_answer_template_int(question: str) -> int:
    user_answer = input_pw(f'{question}', type=NUMBER)
    return user_answer


def compare_answer_with_correct(answer_of_user: str | int, correct_answer: str | int, total_score) -> int:
    if answer_of_user == correct_answer:
        total_score = total_score + 1
    return total_score


def main():
    user_name = ask_and_format_user_name(MSG_GREETING_TEXT)
    first_user_answer = get_user_answer_template_str(MSG_QUESTION_01)
    updated_total_score = compare_answer_with_correct(first_user_answer, MSG_ANSWER_01, total_score)
    second_user_answer = get_user_answer_template_int(MSG_QUESTION_02)
    updated_total_score = compare_answer_with_correct(second_user_answer, MSG_ANSWER_02, updated_total_score)
    third_user_answer = get_user_answer_template_str(MSG_QUESTION_03)
    updated_total_score = compare_answer_with_correct(third_user_answer, MSG_ANSWER_03, updated_total_score)
    fourth_user_answer = get_user_answer_template_str(MSG_QUESTION_04)
    updated_total_score = compare_answer_with_correct(fourth_user_answer, MSG_ANSWER_04, updated_total_score)
    fifth_user_answer = get_user_answer_template_int(MSG_QUESTION_05)
    updated_total_score = compare_answer_with_correct(fifth_user_answer, MSG_ANSWER_05, updated_total_score)

    if updated_total_score == 5:
        put_html(f'<h2>Вітаємо вас, {user_name}! Ви отримали найвищий результат!</h2>')
        img = open('five_stars.jpeg', 'rb').read()
        put_image(img, width='500px')

    if not updated_total_score == 5:
        put_html(f'<h2>Вітаємо вас, {user_name}! Ви набрали {updated_total_score} балів!</h2>')

    run_js('setTimeout(function(){location.reload();}, 10000)')


if __name__ == '__main__':
    start_server(main, port=10000)
