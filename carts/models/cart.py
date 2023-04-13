from django.db import models


class Cart(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"cart @{self.user.username}"
