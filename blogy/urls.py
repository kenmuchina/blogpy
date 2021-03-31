"""Defines URL patterns for blogy."""

from django.urls import path

from . import views

app_name = 'blogy'
urlpatterns = [
    # Home page
    path('', views.index, name='index'), 
    
    # Page that shows all articles
    path('articles/', views.articles, name='articles'),
    
    # Detail page for a single article
    path('articles/<int:article_url>/', views.article, name='article'),
    
    # Page for adding a new article
    path('new_article/', views.new_article, name='new_article'),
    
    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_article, name='edit_entry'),
]

