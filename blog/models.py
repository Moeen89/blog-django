from django.db import models

class Writer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post(models.Model):
    writer = models.ForeignKey(Writer,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")
    image = models.ImageField(upload_to="uploads", blank=True)

    def __str__(self):
        return self.title

