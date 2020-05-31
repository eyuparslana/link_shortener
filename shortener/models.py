from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Site(models.Model):
    url = models.TextField()
    secret_url = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    click_count = models.IntegerField()


class DailyLog(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    log_date = models.DateField()



