from django.db import models


class StatusLivro(models.Model):
    status = models.TextField(max_length=10)

    def __str__(self):
        return self.status
