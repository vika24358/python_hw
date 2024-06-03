from pywebio.output import put_html, put_text, put_image, popup
from pywebio.input import input, slider

import constants_summer_holidays

# header
put_html(constants_summer_holidays.msg_html_header)

# small poem
put_text(constants_summer_holidays.msg_poem_text)

# summer plans text
summer_plans = input(constants_summer_holidays.msg_summer_plans)

# count symbols in summer plans
symbol_count = str(summer_plans).count('')
put_text(f'{constants_summer_holidays.msg_symbol_count} - {symbol_count}')

# picture
img = open('Summer-Holidays-–-How-People-Experience-Time-off-–-Anna-Siampani.jpg', 'rb').read()
put_image(img, width='500px')

# something interesting from documentation
excitement_level = slider(constants_summer_holidays.msg_slider_excitement, min_value=0, max_value=100)
text_popup = popup(constants_summer_holidays.msg_popup_title,
                   f'{constants_summer_holidays.msg_popup_content_01}{excitement_level}{constants_summer_holidays.msg_popup_content_02}')
