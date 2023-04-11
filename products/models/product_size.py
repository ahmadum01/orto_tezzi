from django.db import models


class ProductSize(models.Model):
    size = models.PositiveIntegerField()

    def __str__(self):
        return str(self.size)
