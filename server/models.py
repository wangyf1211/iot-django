from django.db import models


# Create your models here.
class Distance(models.Model):
    distance = models.CharField(max_length=255)
    create_time = models.DateTimeField()

    def __str__(self):
        return self.distance


class Temp(models.Model):
    temp = models.CharField(max_length=255)
    create_time = models.DateTimeField()

    def __str__(self):
        return self.temp
