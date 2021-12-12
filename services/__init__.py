import binascii
import hashlib
import os

from dao import *


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

def service_line_create_message(db, line_obj, json_data):
    dao_line_create_message(db, line_obj, json_data["created_by"], json_data["message"])

    messages = service_line_get_all_messages(line_obj)

    return {"status": 0, "messages": messages}


def service_line_send_message(db, line_obj, json_data):
    pass


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

    dao_line_update_message(db, line_obj, message_id, json_data["message"])

    return service_line_get_message(line_obj, message_id)


def service_line_delete_message(db, line_obj, message_id):
    message_exist = dao_line_get_message(line_obj, message_id)

    status = {"status": 1}

    if message_exist is None:
        return status

    dao_line_delete_message(db, line_obj, message_id)
    status["status"] = 0
    return status


#########
#
# Meetup
#
#########

def service_get_new_member_application(db, new_members_obj):
    new_members_db_list = dao_get_all_new_members(new_members_obj)

    # something like all_apps = mercari_check_new_applications()
    # and then
    # get the meetup id from both and see which one is new, then saved to db the new one

    pass
