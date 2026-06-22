import uuid

from django.conf import settings
from django.db import models


class Notification(models.Model):

    class NotificationType(models.TextChoices):

        INFO = "INFO", "Info"

        SUCCESS = "SUCCESS", "Success"

        WARNING = "WARNING", "Warning"

        ERROR = "ERROR", "Error"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(
        max_length=255
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=20,
        choices=NotificationType.choices,
        default=NotificationType.INFO
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.email} - {self.title}"