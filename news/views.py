from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import News, NewsImages


class MyNews(ListView):
    model = News
    template_name = 'news/news.html'
    context_object_name = 'news'


def load_news(request, slug):
    news = News.objects.all()
    current_obj = get_object_or_404(News, slug=slug)
    images = NewsImages.objects.filter(news__slug=slug)

    paginator = Paginator(news, 1)
    if current_obj in news:
        current_page = list(news).index(current_obj) + 1
    else:
        response = render(request, 'mainFront/page404.html')
        response.status_code = 404
        return response

    page_obj = paginator.get_page(current_page)
    if page_obj.has_previous():
        prev_slug = (news[current_page-2]).slug
    else:
        prev_slug = None
    if page_obj.has_next():
        next_slug = (news[current_page]).slug
    else:
        next_slug = None
    return render(request, 'news/load_news.html', {'page_obj': page_obj,
                                                   'images': images,
                                                   'prev_slug': prev_slug,
                                                   'next_slug': next_slug,
                                                   })
