from django.db import models

class Writer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post(models.Model):
    user_id = models.ForeignKey(Writer,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.title

