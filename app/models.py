from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=20,primary_key=True)
    def __str__(self):
        return self.topic_name

class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,primary_key=True)
    url=models.URLField()
    gmail=models.EmailField(default='https://india.com')
    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=30)
    def __str(self):
        return self.name
