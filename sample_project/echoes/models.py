from django.db import models


class Utterance(models.Model):
    words = models.TextField(help_text='Use reStructuredText here.')


class Echo(models.Model):
    utterance = models.ForeignKey(Utterance, on_delete=models.CASCADE)
    words = models.TextField(help_text='Uses markdown here.')

    class Meta:
        verbose_name_plural = 'echoes'
