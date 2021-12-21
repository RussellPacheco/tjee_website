import base64
import hmac
import binascii
import hashlib
import os
from datetime import datetime
from dao import *
from .utils import send_message


#########
#
# Members
#
#########

def service_create_member(db, member_obj, json_data):
    member_exist = dao_get_member_by_fullname(member_obj, json_data["firstname"], json_data["lastname"])

    status = {"status": 1}

    if member_exist is None:

        dao_create_member(
            db,
            member_obj,
            firstname=json_data["firstname"],
            lastname=json_data["lastname"],
            gender=json_data["gender"],
            country=json_data["country"],
            native_lang=json_data["native_lang"],
            lang_focus=json_data["lang_focus"],
            line_id=json_data["line_id"],
            line_api_id=json_data["line_api_id"],
            meetup_id=json_data["meetup_id"],
            meetup_name=json_data["meetup_name"],
        )

        status["status"] = 0

        return status

    else:
        return status


def service_get_member(member_obj, member_id):
    data = dao_get_member_by_id(member_obj, member_id)

    status = {"status": 1}

    if data is None:
        return status

    json_data = {
        "status": 0,
        "id": data.id,
        "firstname": data.firstname,
        "lastname": data.lastname,
        "gender": data.gender,
        "country": data.country,
        "native_lang": data.native_lang,
        "lang_focus": data.lang_focus,
        "line_id": data.line_id,
        "line_api_id": data.line_api_id,
        "meetup_id": data.meetup_id,
        "meetup_name": data.meetup_name,
        "created_at": data.created_at,
        "last_modified": data.last_modified
    }
    
    return json_data


def service_get_all_members(member_obj):
    data = dao_get_all_members(member_obj)
    
    members = []
    status = {"status": 1}

    if len(data) == 0:
        return status
    
    for member in data:
        json_object = {
            "id": member.id,
            "firstname": member.firstname,
            "lastname": member.lastname,
            "gender": member.gender,
            "country": member.country,
            "native_lang": member.native_lang,
            "lang_focus": member.lang_focus,
            "line_id": member.line_id,
            "line_api_id": member.line_api_id,
            "meetup_id": member.meetup_id,
            "meetup_name": member.meetup_name,
            "created_at": member.created_at,
            "last_modified": member.last_modified
        }

        members.append(json_object)

    return {"members": members, "status": 0}


#########
#
# Admin
#
#########

def service_admin_login(admin_obj, json_data):
    admin_exists = dao_get_admin_by_username(admin_obj, json_data["username"])

    status = {"status": 1}

    if admin_exists is None:
        return status

    salt = admin_exists.password[:64]
    stored_password = admin_exists.password[64:]
    pwdhash = hashlib.pbkdf2_hmac("sha512", json_data["password"].encode("utf-8"), salt.encode("ascii"), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode("ascii")

    if pwdhash == stored_password:
        json_data = {
            "status": 0,
            "user_id": admin_exists.id,
            "username": admin_exists.username
        }
        return json_data
    else:
        status["status"] = -1
        return status


def service_admin_create(db, admin_obj, json_data):
    admin_exist = dao_get_admin_by_username(admin_obj, json_data["username"])

    status = {"status": 1}

    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    hashed_pwd = hashlib.pbkdf2_hmac("sha512", json_data["password"].encode("utf-8"), salt, 100000)
    hashed_pwd = binascii.hexlify(hashed_pwd)

    salt_hashedpwd = (salt + hashed_pwd).decode("ascii")

    if admin_exist is None:

        dao_create_admin(
            db,
            admin_obj,
            member_id=json_data["member_id"],
            username=json_data["username"],
            password=salt_hashedpwd,
        )

        status["status"] = 0

        return status

    else:
        return status


def service_admin_delete(db, admin_obj, json_data):
    admin_to_be_removed_exists = dao_get_admin_by_username(admin_obj, json_data["username_to_be_deleted"])

    status = {"status": 1}

    if admin_to_be_removed_exists is None:
        return status

    admin_exists = dao_get_admin_by_username(admin_obj, json_data["username"])

    if admin_exists is None:
        return status

    salt = admin_exists.password[:64]
    stored_password = admin_exists.password[64:]
    pwdhash = hashlib.pbkdf2_hmac("sha512", json_data["password"].encode("utf-8"), salt.encode("ascii"), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode("ascii")

    if pwdhash == stored_password:
        dao_admin_delete(db, admin_obj, json_data["username_to_be_deleted"])
        status["status"] = 0
        return status
    else:
        status["status"] = -1
        return status


def service_admin_change_password(db, admin_obj, json_data):
    admin_exist = dao_get_admin_by_username(admin_obj, json_data["username"])

    status = {"status": 1}

    if admin_exist is None:
        return status

    salt = admin_exist.password[:64]
    stored_password = admin_exist.password[64:]
    pwdhash = hashlib.pbkdf2_hmac("sha512", json_data["old_password"].encode("utf-8"), salt.encode("ascii"), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode("ascii")

    if pwdhash == stored_password:
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
        hashed_pwd = hashlib.pbkdf2_hmac("sha512", json_data["new_password"].encode("utf-8"), salt, 100000)
        hashed_pwd = binascii.hexlify(hashed_pwd)

        salt_hashedpwd = (salt + hashed_pwd).decode("ascii")

        dao_admin_change_password(db, admin_obj, json_data["username"], salt_hashedpwd)
        status["status"] = 0

        return status
    else:
        status["status"] = -1
        return status


#########
#
# Line
#
#########

def service_line_webhook(db, webhook_obj, bot_permission_obj, headers, json_data):

    print("GOT A WEBHOOK")
# def service_line_webhook(db, webhook_obj, json_data):

    # Useful 'type'
    #
    # message - Webhook event object which contains the sent message.
    # join - Event object for when your LINE Account joins a group or room. You can reply to join events.

    # follow - Event object for when your LINE Official Account is added as a friend (or unblocked).
    # unfollow - Event object for when your LINE Official Account is blocked.
    # just userId

    # leave - Event object for when a user removes your LINE Official Account from a group or when your LINE Official Account leaves a group or room.
    # memberJoined - Event object for when a user joins a group or room that the LINE Official Account is in.
    # memberLeft - Event object for when a user leaves a group or room that the LINE Official Account is in.
    # userId, groupId

    # Example webhook event
    # {
    #     "destination": "xxxxxxxxxx",
    #     "events": [
    #         {
    #             "type": "message",
    #             "message": {
    #                 "type": "text",
    #                 "id": "14353798921116",
    #                 "text": "Hello, world"
    #             },
    #             "timestamp": 1625665242211,
    #             "source": {
    #                 "type": "user",
    #                 "userId": "U80696558e1aa831..."
    #             },
    #             "replyToken": "757913772c4646b784d4b7ce46d12671",
    #             "mode": "active"
    #         },
    #         {
    #             "type": "follow",
    #             "timestamp": 1625665242214,
    #             "source": {
    #                 "type": "user",
    #                 "userId": "Ufc729a925b3abef..."
    #             },
    #             "replyToken": "bb173f4d9cf64aed9d408ab4e36339ad",
    #             "mode": "active"
    #         },
    #         {
    #             "type": "unfollow",
    #             "timestamp": 1625665242215,
    #             "source": {
    #                 "type": "user",
    #                 "userId": "Ubbd4f124aee5113..."
    #             },
    #             "mode": "active"
    #         }
    #     ]
    # }

    channel_secret = os.getenv("CHANNEL_SECRET")
    header_hash = hmac.new(channel_secret.encode('utf-8'), json_data.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b85decode(header_hash)

    if signature == headers['x-line-signature']:
        status = {"status": 1}

        for event in json_data["events"]:

            EVENT_TYPE = event["type"] if hasattr(event, "type") else None
            TIMESTAMP = datetime.fromtimestamp(event["timestamp"] / 1000.0) if hasattr(event, "timestamp") else None
            USER_ID = event["source"]["userId"] if hasattr(event["source"], "userId") else None
            GROUP_ID = event["source"]["groupId"] if hasattr(event["source"], "groupId") else None

            if EVENT_TYPE in ["follow", "unfollow", "message"]:
                if EVENT_TYPE == "message":
                    exists = dao_line_get_webhook(webhook_obj, line_type=EVENT_TYPE, userId=USER_ID)
                    if exists is None:
                        dao_line_save_webhook(db, webhook_obj, line_type=EVENT_TYPE, timestamp=TIMESTAMP, userId=USER_ID, message=event["message"]["text"])
                else:
                    dao_line_save_webhook(db, webhook_obj, line_type=EVENT_TYPE, timestamp=TIMESTAMP, userId=USER_ID)
            elif EVENT_TYPE in ["join", "leave", "memberJoined", "memberLeft"]:
                dao_line_save_webhook(db, webhook_obj, line_type=EVENT_TYPE, timestamp=TIMESTAMP, groupId=GROUP_ID, userId=USER_ID)
                if EVENT_TYPE == "join":
                    allowed = dao_line_get_bot_permission(bot_permission_obj, permission_name="group_join")
                    if allowed.permission:

                        text = """
                        
                        Thank you for inviting me! 
                        
                        """

                        send_message("reply", event["replyToken"], text)

                # I WILL LEAVE THIS HERE IN CASE I NEED THIS IN THE FUTURE
                # elif event["source"]["type"] == "room":
                #     exists = dao_line_get_webhook(webhook_obj, roomId=event["source"]["roomId"])
                #
                # if exists is None: dao_line_save_webhook(db, webhook_obj, line_type=EVENT_TYPE,
                # timestamp=TIMESTAMP, roomId=event["source"]["roomId"])

            status["status"] = 0
            return status
        else:
            return status


def service_line_change_bot_permission(db, bot_permission_obj, permission, json_data):

    status = {"status": 1}
    permission_name = json_data["permission_name"]
    last_modified = datetime.now()

    exists = dao_line_get_bot_permission(bot_permission_obj, permission_name=permission_name)

    if exists:
        dao_line_change_bot_permission(db, bot_permission_obj, permission_name=permission_name, permission=permission, last_modified=last_modified)
        status["status"] = 0
        return status
    else:
        return status


def service_line_get_bot_permissions(bot_permission_obj):
    data = dao_line_get_all_bot_permissions(bot_permission_obj)

    permissions = []

    status = {"status": 1}

    if len(data) == 0:
        return status

    for permission in data:
        json_obj = {
            "id": permission.id,
            "permission_name": permission.permission_name,
            "message": permission.permission_value,
            "last_modified": permission.last_modified
        }

        permissions.append(json_obj)

    return {"status": 0, "permissions": permissions}


def service_line_create_message(db, line_obj, json_data):
    dao_line_create_message(db, line_obj, json_data["created_by"], json_data["message"])

    messages = service_line_get_all_messages(line_obj)

    return messages


def service_line_send_message(db, line_obj, json_data):

    status = {"status": 1}
    MESSAGE = json_data["message"]
    DESTINATION = json_data["destination"]

    result = send_message("push", DESTINATION, MESSAGE)

    if result != 0:
        status["error"] = result
        return status

    dao_line_update_message_time(db, line_obj, json_data["message_id"], datetime.now())

    return status


def service_line_get_all_messages(line_obj):
    data = dao_line_get_all_messages(line_obj)

    messages = []

    status = {"status": 1}

    if len(data) == 0:
        return status

    for message in data:
        json_obj = {
            "id": message.id,
            "created_by": message.created_by,
            "message": message.message,
            "created_at": message.created_at,
            "last_sent": message.last_sent,
            "last_modified": message.last_modified
        }

        messages.append(json_obj)

    return {"status": 0, "messages": messages}


def service_line_get_message(line_obj, message_id):
    message = dao_line_get_message(line_obj, message_id)

    status = {"status": 1}

    if message is None:
        return status

    json_obj = {
        "status": 0,
        "id": message.id,
        "created_by": message.created_by,
        "message": message.message,
        "created_at": message.created_at,
        "last_sent": message.last_sent,
        "last_modified": message.last_modified
    }

    return json_obj


def service_line_update_message(db, line_obj, message_id, json_data):
    message = dao_line_get_message(line_obj, message_id)

    status = {"status": 1}

    if message is None:
        return status

    dao_line_update_message(db, line_obj, message_id, json_data["message"], datetime.now())

    return service_line_get_message(line_obj, message_id)


def service_line_delete_message(db, line_obj, message_id):
    message_exist = dao_line_get_message(line_obj, message_id)

    status = {"status": 1}

    if message_exist is None:
        return status

    dao_line_delete_message(db, line_obj, message_id)
    return service_line_get_all_messages(line_obj)


#########
#
# Meetup
#
#########

def service_get_new_member_application(db, new_members_obj):
    # new_members_db_list = dao_get_all_new_members(new_members_obj)

    # something like all_apps = mercari_check_new_applications()
    # and then
    # get the meetup id from both and see which one is new, then saved to db the new one

    pass
