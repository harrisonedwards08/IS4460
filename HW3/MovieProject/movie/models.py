from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length = 100,default = "")
    description = models.CharField(max_length = 500)
    director = models.CharField(max_length = 100)
    release_year = models.IntegerField(max_length = 50)
    budget = release_year = models.IntegerField(max_length = 50)
    runtime = models.IntegerField(max_length = 50)
    rating = models.CharField(max_lenth = 50)

class User(models.Model):
    username = models.CharField(max_length = 50,default = "")
    password = models.CharField(max_length = 255,default = "")
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)


    