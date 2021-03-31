from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    email = models.EmailField()
    contact = models.IntegerField()
    field = models.CharField(max_length=20)
    about = models.CharField(max_length=50)
    
    # Requires Pillow Python package
    # pip install Pillow
    # profile_pic = models.ImageField()
