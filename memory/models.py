from django.db import models


class Folder(models.Model):
    title = models.CharField(max_length=100)

class Memory(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='memory_images/', blank=True, null=True)
    date = models.DateField()
    content = models.TextField()




# Create your models here.
