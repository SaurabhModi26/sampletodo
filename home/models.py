from django.db import models

# Create your models here.
class Task(models.Model):
    TaskTitle = models.CharField(max_length=30)
    TaskDesc = models.TextField(max_length=1000)
    TaskTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.TaskTitle