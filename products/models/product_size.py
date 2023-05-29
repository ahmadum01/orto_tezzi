from django.db import models


class ProductSize(models.Model):
    size = models.CharField(max_length=15)

    def __str__(self):
        return str(self.size)
