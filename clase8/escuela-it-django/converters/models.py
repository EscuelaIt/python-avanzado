from django.db import models


class Currency(models.Model):
    key = models.CharField(max_length=3, null=False, blank=False)
    country = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return f"{self.key}, {self.country}"
