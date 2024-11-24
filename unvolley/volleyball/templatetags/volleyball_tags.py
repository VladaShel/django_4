from django import template
import volleyball.views as views
from volleyball.models import Category, TagTeam

register = template.Library()

@register.inclusion_tag('volleyball/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected_id}

@register.inclusion_tag('volleyball/list_tags.html')
def show_all_tags():
    return {"tags": TagTeam.objects.all()}
