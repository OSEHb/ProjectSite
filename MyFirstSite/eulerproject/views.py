from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Problems


def problems(request):
    problems_list = Problems.objects.all().order_by("id")  # вызываем все объекты и сортируем по id

    context = {}  # словарь
    paginator = Paginator(problems_list, 5)  # Что разбиваем и на сколько частей
    page = request.GET.get('page')  # принимаемый запрос
    try:
        context['problems_list'] = paginator.page(page)  # Если существует, то выбираем эту страницу
    except PageNotAnInteger:
        context['problems_list'] = paginator.page(1)  # Если None, то выбираем первую страницу
    except EmptyPage:
        context['problems_list'] = paginator.page(paginator.page.num_pages)  # Если вышли за последнюю страницу, то возвращаем последнюю

    return render(request, 'eulerproject/eulerpage.html', context)
