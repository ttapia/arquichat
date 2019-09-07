from django.db import models
from django.utils.timezone import now

class Message(models.Model):
    author = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=now, editable=False);
