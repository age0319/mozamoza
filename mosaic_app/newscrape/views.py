from django.shortcuts import render
from . import scraping_news
from .form import SearchForm


def index(request):

    entry_num = 15

    params = {
        'form': SearchForm()
    }

    if request.method == 'POST':

        keyword = request.POST['keyword']
        articles = scraping_news.scrape_news(keyword, entry_num)

        params = {
            'articles': articles,
            'form': SearchForm(request.POST)
        }

    return render(request, 'top.html', params)
