from django.db import models


class Echo(models.Model):
    words = models.TextField()

    class Meta:
        verbose_name_plural = 'echoes'
