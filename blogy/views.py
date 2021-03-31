from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    # Render the home page that contains the general feel of the website
    return render(request, 'blogy/index.html')

def articles(request):
    # query all articles
    # articles = Article.objects.all().order_by()

    # I'll be using in_bulk since it returns a dictionary
    articles = Article.objects.in_bulk().order_by('timestamp')

    # pass all articles to the templates
    return render(request, 'blogy/articles.html', {'articles': articles})

def article(request):
    # Get the params url
    article_url = request.params.article_url
    # Query the database using the url of the article
    article = Article.objects.get(url=article_url)
    return render(request, 'blogy/article.html', {'article':  article})

def new_article(request):
    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = Article(request.POST)
        # check if it's valid
        if form.is_valid():
            # Insert into DB
            form.save()
            # redirect to a new URL
            return HttpResponseRedirect('blogy/articles.html')
        else:
            # GET, generate unobound (blank) form
            form = Article()
        return render(request, 'blogy/new_article.html', {'form': form})
    

def edit_article(request):
    pass



