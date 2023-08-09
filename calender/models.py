from django.db import models

# Create your models here.

class IslamicCalender(models.Model):
    gregorian_date = models.DateField()