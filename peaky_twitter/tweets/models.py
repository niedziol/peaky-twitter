from django.conf import settings
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    author = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )
    body = models.TextField()
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.author)