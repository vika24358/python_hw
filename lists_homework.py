from pywebio.input import textarea, select, slider, checkbox, radio, input as input_pw
from pywebio.output import put_success, put_html
from pywebio.session import run_js
from pywebio import start_server

genre_options = ["Комедія",
                 "Драма",
                 "Бойовик",
                 "Пригоди",
                 "Фантастика",
                 "Фентезі",
                 "Жахи",
                 "Романтика",
                 "Детектив",
                 "Документальний",
                 ]
emotions_options = [
    "Радість",
    "Смуток",
    "Страх",
    "Гнів",
    "Здивування",
    "Ностальгія",
    "Співчуття",
    "Напруга",
    "Спокій",
    "Захоплення",
    "Розчарування",
    "Нудьгу",
    "Інтерес",
]

reviews_info = []


def main():
    put_html('<h1>Програма збору відгуків на фільми</h1>')
    username = input_pw("Введіть ваше ім'я")
    film_name = input_pw("Введіть назву фільму")
    film_genre = select("Виберіть жанр фільму", options=genre_options)
    film_review_text = textarea("Напишіть невеликий відгук на фільм")
    film_rating = slider("Наскільки вам сподобався фільм?", min_value=1, max_value=10)
    film_emotions = checkbox("Які емоції викликав у вас цей фільм?", options=emotions_options)
    film_recommendation = radio("Чи рекомендуєте ви цей фільм іншим людям", options=["Так", "Ні"])

    if film_rating >= 7:
        put_success("Ваш відгук успішно збережено! Дякуємо!")

    reviews_info.append(
        [username, film_name, film_genre, film_review_text, film_rating, film_emotions, film_recommendation])
    run_js('setTimeout(function(){location.reload();}, 4000)')


if __name__ == '__main__':
    start_server(main, port=11000)
