from django.db import models

class News(models.Model):
    publishers = models.CharField(max_length=200)
    titles = models.CharField(max_length=3000)
    count = models.IntegerField(default=0)



