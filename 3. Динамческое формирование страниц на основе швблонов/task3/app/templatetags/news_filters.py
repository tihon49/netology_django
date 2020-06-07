import time
from django import template


register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    now = time.time()
    value = float(value)
    if (now - value) / 60 < 10:
        return 'только что'
    elif (now - value) / 60 / 60 < 24:
        return f'{int((now - value) / 60 / 60)} часов назад'
    elif (now - value) / 60 / 60 > 24:
        return time.ctime(value)



# необходимо добавить фильтр для поля `score`
@register.filter
def score_filter(value):
    if value < -5:
        return 'все плохо'
    elif -5 < value < 5:
        return 'нейтрально'
    elif value > 5:
        return 'хорошо'
    else:
        return 'нет рейтинга'



@register.filter
def format_num_comments(value):
    # Ваш код
    if value == 0:
        return 'оставьте комментарий'
    elif 0 < value < 50:
        return value
    elif value > 50:
        return '50+'



@register.filter
def format_selftext(value, num=3):
    if len(value.split()) > num:
        return f'{" ".join(value.split()[:num])} ... {" ".join(value.split()[-num:])}'
    else:
        return value