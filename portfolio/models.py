from django.db import models


class Mail(models.Model):
    name = models.CharField(max_length=100, default="default_name")
    sender = models.EmailField(default="default_email@mail.dk")
    subject = models.CharField(max_length=100, default="default_subject")
    message = models.TextField(default="default_message")
    created_at = models.DateTimeField(auto_now_add=True)
