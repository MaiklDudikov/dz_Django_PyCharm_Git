from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
