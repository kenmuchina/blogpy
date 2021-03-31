from django.db import models
from .Author import Author

class Article(models.Model):
    url = models.SlugField(max_length=30)
    title = models.CharField(max_length=20)
    
    # Not sure which is appropriate
    content = models.TextField()
    # content = models.CharField(), unfortunately we can't estimate the max_length of an articl
    # That's how I choose to use TextField() instead
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    timestamp = models.DateTimeField(auto_now_add=True)



