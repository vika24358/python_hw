from pywebio.input import textarea, select, slider, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw
from pywebio.output import put_success, put_error, put_warning, put_image, put_html
from pywebio.session import run_js
from pywebio import start_server

admin_one_login = 'aaa'
admin_one_password = '123'

bad_weather = ["Хмарно", 'Шторм']
good_weather = ['Сонячно']
weather_options = bad_weather + good_weather

monitoring_info = []

emotions = ["Круто", "Весело", "Сумно", "Набридло"]


def main():
    put_html('<h1>Програма моніторингу погоди</h1>')
    login = input_pw('Введіть ваш логін', required=True)
    password = input_pw('Введіть ваш пароль', type=PASSWORD, required=True)

    if login != admin_one_login or password != admin_one_password:
        put_error('Невірний логін або пароль')
        run_js('setTimeout(function(){location.reload();}, 6000)')
        return

    monitoring_date = input_pw("Введіть дату спостереження", type=DATE)
    weather = select('Яка сьогодні погода?', options=weather_options)
    if weather in good_weather:
        put_success('Супер, що класно погуляв')

    short_description = textarea('Опишіть природу сьогодні')
    temperature = slider('Опишіть, яка сьогодні температура', min_value=-35, max_value=50)
    your_emotions = checkbox("Які у вас емоції?", options=emotions)
    alone = radio("Ви були самі?", options=[True, False])
    if alone:
        put_image(
            'https://static.vecteezy.com/system/resources/thumbnails/030/024/454/small_2x/rising-meditation-silence-reflection-rest-lake-landscape-silence-zen-relaxation-lonely-woman-photo.jpg')
    else:
        put_image('https://img.huffingtonpost.com/asset/604fc2f2260000cc17d854ff.jpeg?cache=htB0uiPrAE&ops=1778_1000')

    monitoring_info.append([monitoring_date, weather])
    run_js('setTimeout(function(){location.reload();}, 6000)')


if __name__ == '__main__':
    start_server(main, port=11000)
