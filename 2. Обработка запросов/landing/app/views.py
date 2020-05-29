from collections import Counter
from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    if request.GET.get('from-landing') == 'original':
        counter_click['original'] += 1
        print(counter_click)
    elif request.GET.get('from-landing') == 'test':
        counter_click['test'] += 1
        print(counter_click)
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    # if request.GET.get('landing'):
    counter_show['original'] += 1
    print(counter_show)
    return render_to_response('landing.html')

def landing_alternate(request):
    counter_show['test'] += 1
    print(counter_show)
    return render_to_response('landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    try:
        test = counter_click['test'] / counter_show['test']
    except ZeroDivisionError:
        test = 0

    try:
        original = counter_click['original'] / counter_show['original']
    except ZeroDivisionError:
        original = 0

    return render_to_response('stats.html', context={
        'test_conversion': round(test, 2),
        'original_conversion': round(original, 2),
    })
