from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .models import Article, Category, Tag
from apps.comments.models import Comment
from apps.comments.forms import CommentForm
from django.db.models import Q


def index(request):
    articles = Article.objects.all()
    # pagination
    page_number = request.GET.get("page")
    p = Paginator(articles, 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    except EmptyPage:
        page_obj = p.get_page(p.num_pages)

    context = {"articles": articles, "p": p, "page_obj": page_obj}
    return render(request, 'index.html', context)


def article(request):
    articles = Article.objects.all()
    # Category
    categories = Category.objects.all()
    # Tag
    tags = Tag.objects.all()
    # Pagination
    category = request.GET.get('category')
    if category:
        articles = Article.objects.filter(category__title__exact=category)

    tag = request.GET.get("tag")
    if tag:
        articles = Article.objects.filter(tags__title__exact=tag)

    q = request.GET.get("q")
    if q:
        articles = Article.objects.distinct().filter(Q(title__icontains=q) |
                                                     Q(context__icontains=q) |
                                                     Q(category__title__icontains=q) |
                                                     Q(tags__title__icontains=q)
                                                     )

    page_number = request.GET.get("page")
    p = Paginator(articles, 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    except EmptyPage:
        page_obj = p.get_page(p.num_pages)

    context = {"articles": articles, "p": p,
               "categories": categories, "tags": tags, "page_obj": page_obj
               }
    return render(request, 'blog.html', context)


def views_up(request, pk):
    obj = Article.objects.get(id=pk)
    obj.views += 1
    obj.save()
    return redirect('articles:single-article', obj.id)


def single_article(request, pk):
    article = Article.objects.get(id=pk)
    recent_articles = Article.objects.all().order_by("-created_at")[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    # views
    comments = Comment.objects.filter(article=article)
    # comment with form
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            obj1 = form.save(commit=False)
            obj1.article = article
            obj1.save()
            return redirect('articles:single-article', pk)

    context = {"article": article, "form": form, "categories": categories,
               "tags": tags, "recent_articles": recent_articles,
               "comments": comments
               }
    return render(request, 'blog-single.html', context)
