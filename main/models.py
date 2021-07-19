from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    desc = models.TextField()
    now = models.DateTimeField()

    def __str__(self) -> str:
        return self.email
