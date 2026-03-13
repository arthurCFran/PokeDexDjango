from django.db import models

# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    level = models.IntegerField()

    def __str__(self):
        return self.name