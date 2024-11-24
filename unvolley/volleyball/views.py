from IPython.core.completerlib import is_possible_submodule
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from volleyball.models import Volleyball, Category, TagTeam

menu = [{'title': "Войти", 'url_name': 'login'},
        {'title':"Рейтинг", 'url_name': 'rating'},
        {'title':"Турниры", 'url_name': 'competitions'},
        {'title': "О сайте", 'url_name': 'about'},
]

cats_db = [
    {'id': 1, 'name': 'Тренера'},
    {'id': 2, 'name': 'Игроки'},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'team': Volleyball.published.all(),
        'cat_selected': 0,
    }
    return render(request, 'volleyball/index.html', context=data)

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Категории</h1><p >slug: {cat_slug}</p>")

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    team = Volleyball.published.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'team': team,
        'cat_selected': category.pk,
    }
    return render(request, 'volleyball/index.html', context=data)


def show_tag_teamlist(request, tag_slug):
    tag = get_object_or_404(TagTeam, slug=tag_slug)
    team = tag.tags.filter(is_published=Volleyball.Status.PUBLISHED)

    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'team': team,
        'cat_selected': None,
    }

    return render(request, 'volleyball/index.html', context=data)


def archive(request, year):
    if year > 2024:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def about(request):
    return render(request, 'volleyball/about.html', {'title': 'О сайте', 'menu': menu})


def show_team(request, team_slug):
    team = get_object_or_404(Volleyball, slug = team_slug)

    data = {
        'title': team.title,
        'menu': menu,
        'team': team,
        'cat_selected': 1,
    }

    return render(request, 'volleyball/team.html', context=data)

def rating(request):
    return HttpResponse("Рейтинг")

def competitions(request):
    return HttpResponse("Турниры")

def login(request):
    return HttpResponse("Авторизация")


