from django.db import models

# Create your models here.
class MyModel(models.Model):
    field1 = models.CharField(max_length=50)
    field2 = models.CharField(max_length=50)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title