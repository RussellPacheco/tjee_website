from itsdangerous import json
from services import *


#########
#
# Members
#
#########


def controller_create_member(db, member_obj, json_data):
    try:
        data = service_create_member(db, member_obj, json_data)
        return data

    except Exception as e:
        print(e)
        return {"status": -1}


def controller_get_member(member_obj, member_id):
    try:
        data = service_get_member(member_obj, member_id)
        return data

    except Exception as e:
        print(e)
        return str(e)


def controller_get_all_members(member_obj):
    try:
        data = service_get_all_members(member_obj)
        return data

    except Exception as e:
        print(e)
        return str(e)

def controller_member_update(db, member_obj, json_data):
    try:
        data = service_member_update(db, member_obj, json_data)
        return data
    except Exception as e:
        print(e)
        return str(e)


#########
#
# Admin
#
#########


def controller_admin_login(admin_obj, json_data):
    try:
        data = service_admin_login(admin_obj, json_data)
        return data

    except Exception as e:
        print(e)
        return str(e)


def controller_admin_get_all(admin_obj):
    try:
        data = service_admin_get_all(admin_obj)
        return data
    except Exception as e:
        print(e)
        return str(e)


def controller_admin_create(db, admin_obj, json_data):
    try:
        data = service_admin_create(db, admin_obj, json_data)
        return data

    except Exception as e:
        print(e)
        return str(e)


def controller_admin_delete(db, admin_obj, json_data):
    try:
        data = service_admin_delete(db, admin_obj, json_data)
        return data

    except Exception as e:
        print(e)
        return str(e)


def controller_admin_change_password(db, admin_obj, json_data):
    try:
        data = service_admin_change_password(db, admin_obj, json_data)
        return data

    except Exception as e:
        print(e)
        return str(e)


#########
#
# Line
#
#########

def controller_line_webhook(db, webhook_obj, bot_permission_obj, body, headers, json_data):
    try:
        data = service_line_webhook(db, webhook_obj, bot_permission_obj, body, headers, json_data)
        print("in controller")
        return data
    except Exception as e:
        print(e)
        return str(e)


def controller_line_change_bot_permission(db, bot_permission_obj, json_data):
    try:
        data = service_line_change_bot_permission(db, bot_permission_obj, json_data)
        return data
    except Exception as e:
        print(e)
        return str(e)


def controller_line_get_bot_permissions(bot_permission_obj):
    try:
        data = service_line_get_bot_permissions(bot_permission_obj)
        return data
    except Exception as e:
        print(e)
        return str(e)


def controller_line_create_message(db, line_obj, json_data):
    try:
        data = service_line_create_message(db, line_obj, json_data)
        return data

    except Exception as e:
        print(e)
        return str(e)


def controller_line_send_message(db, line_obj, json_data):
    try:
        data = service_line_send_message(db, line_obj, json_data)
        return data

    except Exception as e:
        print(e)
        return str(e)


def controller_line_get_all_messages(line_obj):
    try:
        data = service_line_get_all_messages(line_obj)
        return data

    except Exception as e:
        print(e)
        return str(e)


def controller_line_get_message(line_obj, message_id):
    try:
        data = service_line_get_message(line_obj, message_id)
        return data

    except Exception as e:
        print(e)
        return str(e)


def controller_line_update_message(db, line_obj, message_id, json_data):
    try:
        data = service_line_update_message(db, line_obj, message_id, json_data)
        return data

    except Exception as e:
        print(e)
        return str(e)


def controller_line_delete_message(db, line_obj, message_id):
    try:
        data = service_line_delete_message(db, line_obj, message_id)
        return data

    except Exception as e:
        print(e)
        return str(e)


#########
#
# Meetup
#
#########

def controller_get_new_member_applications(new_members_obj):
    try:
        data = service_get_new_member_applications(new_members_obj)
        return data

    except Exception as e:
        print(e)
        return str(e)


def controller_update_new_member_applications():
    try:
        data = service_update_new_member_applications()
        return data
    except Exception as e:
        print(e)
        return str(e)


def controller_approve_new_member(db, new_member_obj, json_obj):
    try:
        data = service_approve_new_member(db, new_member_obj, json_obj)
        return data
    except Exception as e:
        print(e)
        return str(e)


def controller_deny_new_member(db, new_member_obj, json_obj):
    try:
        data = service_deny_new_member(db, new_member_obj, json_obj)
        return data
    except Exception as e:
        print(e)
        return str(e)


def controller_get_current_members(member_obj):
    try:
        data = service_get_current_members(member_obj)
        return data
    except Exception as e:
        print(e)
        return str(e)


def controller_get_current_events():
    try:
        data = service_get_current_events()
        return data
    except Exception as e:
        print(e)
        return str(e)