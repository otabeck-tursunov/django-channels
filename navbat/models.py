from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
