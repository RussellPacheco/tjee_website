from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import os


def send_message(msg_type, destination, text):
    line_bot_api = LineBotApi(os.getenv("CONNECTION_TOKEN"))

    if msg_type == "reply":
        try:
            line_bot_api.reply_message(destination, TextSendMessage(text=text))
        except LineBotApiError as e:
            return e
    elif msg_type == "push":
        try:
            line_bot_api.push_message(destination, TextSendMessage(text=text))
        except LineBotApiError as e:
            return e

    return 0
