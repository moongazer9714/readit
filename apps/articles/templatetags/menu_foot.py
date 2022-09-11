from django import template
from apps.articles.models import Article

register = template.Library()


@register.inclusion_tag("menu_foot.html")
def show_foot(menu_class='ftco-footer ftco-bg-dark ftco-section'):
    articles = Article.objects.all().order_by("-created_at")[:2]
    return {"articles": articles, 'menu_class': menu_class}
