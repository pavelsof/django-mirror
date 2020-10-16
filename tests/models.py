from django.db import models


class Echo(models.Model):
    words = models.TextField()


class EchoReply(models.Model):
    echo = models.ForeignKey(Echo, on_delete=models.CASCADE)
    words = models.TextField()
