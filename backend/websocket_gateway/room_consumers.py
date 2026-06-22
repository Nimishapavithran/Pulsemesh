import json

from channels.generic.websocket import (
    AsyncWebsocketConsumer
)


class RoomConsumer(
    AsyncWebsocketConsumer
):

    async def connect(self):

        user = self.scope["user"]

        if not user:

            await self.close()

            return

        self.room_id = self.scope[
            "url_route"
        ]["kwargs"]["room_id"]

        self.room_group_name = (
            f"room_{self.room_id}"
        )

        await self.channel_layer.group_add(

            self.room_group_name,

            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(

            self.room_group_name,

            {
                "type": "presence_event",

                "message": f"{user.email} joined room",
            }
        )

    async def disconnect(
        self,
        close_code
    ):

        user = self.scope["user"]

        await self.channel_layer.group_send(

            self.room_group_name,

            {
                "type": "presence_event",

                "message": f"{user.email} left room",
            }
        )

        await self.channel_layer.group_discard(

            self.room_group_name,

            self.channel_name
        )

    async def receive(
        self,
        text_data
    ):

        data = json.loads(text_data)

        message = data.get(
            "message"
        )

        user = self.scope["user"]

        await self.channel_layer.group_send(

            self.room_group_name,

            {
                "type": "chat_message",

                "message": message,

                "user": user.email,
            }
        )

    async def chat_message(
        self,
        event
    ):

        await self.send(
            text_data=json.dumps(
                {
                    "type": "chat",

                    "user": event["user"],

                    "message": event["message"],
                }
            )
        )

    async def presence_event(
        self,
        event
    ):

        await self.send(
            text_data=json.dumps(
                {
                    "type": "presence",

                    "message": event["message"],
                }
            )
        )