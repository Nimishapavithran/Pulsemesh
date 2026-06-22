import uuid

from django.conf import settings
from django.db import models


class Room(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=255,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE,

        related_name="created_rooms"
    )

    members = models.ManyToManyField(

        settings.AUTH_USER_MODEL,

        related_name="rooms",

        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.name