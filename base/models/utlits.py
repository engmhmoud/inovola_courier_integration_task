from django.db import models


class Dimension(models.Model):
    METRIC_CHOICE = 0

    UNITE_CHOICES = ((METRIC_CHOICE, "METRIC"))
    weight = models.FloatField()
    width = models.FloatField()
    length = models.FloatField()
    height = models.FloatField()
    unit = models.CharField(choices=UNITE_CHOICES, max_length=1)
    domestic = models.BooleanField()
