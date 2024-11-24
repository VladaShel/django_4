from django.contrib import admin
from django.urls import path, include, register_converter
from volleyball import views, converters

register_converter(converters.FourDigitYearConverter,"year4")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    path('archive/<year4:year>/', views.archive, name='archive'),
    path('rating/', views.rating, name='rating'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('competitions/', views.competitions, name='competitions'),
    path('team/<slug:team_slug>/', views.show_team, name='team'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_teamlist, name='tag'),
]

handler404 = views.page_not_found
