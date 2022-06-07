from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creaeted = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    class Meta:
        ordering = ['-creaeted']
    
    def __str__(self):
        return self.title
    
    