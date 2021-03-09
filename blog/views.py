from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.models import User
from .models import Article, Category


# Create your views here.
# def home(request, page=1):
#     articles_list = Article.objects.published()
#     paginator = Paginator(articles_list, 4)
#     articles = paginator.get_page(page)
#     context = {
#         "articles": articles,
#     }
#     return render(request, "blog/home.html", context)

class ArticleList(ListView):
    queryset = Article.objects.published()
    context_object_name = "articles"
    paginate_by = 4
    template_name = "blog/home.html"

# def detail(request, slug):
#     context = {
#         "article": get_object_or_404(Article.objects.published(), slug=slug),
#     }
#     return render(request, "blog/detail.html", context)

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)

# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     articles_list = category.articles.published()
#     paginator = Paginator(articles_list, 2)
#     articles = paginator.get_page(page)
#     context = {
#         "category": category,
#         "articles": articles
#     }
#     return render(request, "blog/category.html", context)

class CategoryList(ListView):
    paginate_by = 2

    template_name = "blog/category.html"

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

class AuthorList(ListView):
    paginate_by = 2

    template_name = "blog/author_list.html"

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context

