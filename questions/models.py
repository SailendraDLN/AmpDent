from django.db import models

# Create your models here.
class question(models.Model):
    topic = models.CharField(max_length=50)
    content = models.TextField()
    marks = models.IntegerField()
    asked = models.IntegerField()
    subject = models.CharField(max_length=50)
    #probability will be added in the future
