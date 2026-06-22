from asgiref.sync import async_to_sync

from celery import shared_task

from channels.layers import get_channel_layer

from accounts.models import User

from .models import Notification


@shared_task
def send_realtime_notification(

    user_id,
    title,
    message,
    notification_type="INFO"
):

    user = User.objects.get(
        id=user_id
    )

    notification = Notification.objects.create(

        user=user,

        title=title,

        message=message,

        notification_type=notification_type,
    )

    channel_layer = get_channel_layer()

    async_to_sync(
        channel_layer.group_send
    )(

        f"user_{user.id}",

        {
            "type": "send_notification",

            "message": {

                "id": str(notification.id),

                "title": notification.title,

                "message": notification.message,

                "notification_type": notification.notification_type,
            },
        }
    )