from django.db import models
from django.contrib.auth.models import (AbstractUser)


class TwitterUser(AbstractUser):
    following = models.ManyToManyField(
        "self", symmetrical=False, blank=True)

    def __str__(self):
        return self.username

    @property
    def displayname(self):
        return self.first_name + " " + self.last_name