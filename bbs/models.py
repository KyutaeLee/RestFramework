from django.db import models

# Create your models here.

class Bbs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, blank=True, default=True)
    pw = models.CharField(max_length=12, blank=True, default=True)
    title = models.CharField(max_length=100, blank=True, default=True)
    content = models.TextField()

    class Meta:
        ordering = ('created',)

