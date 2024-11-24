from django.urls import path, register_converter
from volleyball import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    path('archive/<year4:year>/', views.archive, name='archive'),
    path('rating/', views.rating, name='rating'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('competitions/', views.competitions, name='competitions'),
    path('team/<int:team_id>/', views.show_team, name='team'),
]


#register_converter(FourDigitYearConverter, "year4")
