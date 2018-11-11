from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Media(models.Model):
    name = models.CharField(max_length=140)
    upload = models.FileField(upload_to='%Y/%m/%d/')

    def __str__(self):
        return self.name

class Page(models.Model):
    name = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name
