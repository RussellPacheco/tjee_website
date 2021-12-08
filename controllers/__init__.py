from flask import json
from services import *


#########
#
# Members
#
#########


def controller_create_member(db, member_obj, admin_obj, json_data):
    try:
        data = service_create_member(db, member_obj, admin_obj, json_data)
        return data

    except Exception as e:
        return str(e)


def controller_get_member(member_obj, member_id):
    try:
        data = service_get_member(member_obj, member_id)
        return data

    except Exception as e:
        return str(e)


def controller_get_all_members(member_obj):
    try:
        data = service_get_all_members(member_obj)
        return data

    except Exception as e:
        return str(e)


#########
#
# Admin
#
#########


def controller_admin_login(db, admin_obj, json_data):
    try:
        data = service_admin_login(db, admin_obj, json_data)
        return data

    except Exception as e:
        return str(e)


def controller_admin_create(db, member_obj, admin_obj, json_data):
    try:
        data = service_admin_create(db, admin_obj, json_data)
        return data

    except Exception as e:
        return str(e)


def controller_admin_delete(db, admin_obj, json_data):
    try:
        data = service_admin_delete(db, admin_obj, json_data)
        return data

    except Exception as e:
        return str(e)


def controller_admin_change_password(db, admin_obj, json_data):
    try:
        data = service_admin_change_password(db, admin_obj, json_data)
        return data

    except Exception as e:
        return str(e)


#########
#
# Line
#
#########

def controller_line_create_message(db, line_obj, json_data):
    try:
        data = service_line_create_message(db, line_obj, json_data)
        return data

    except Exception as e:
        return str(e)


def controller_line_send_message(db, line_obj, json_data):
    try:
        data = service_line_send_message(db, line_obj, json_data)
        return data

    except Exception as e:
        return str(e)


def controller_line_get_all_messages(line_obj):
    try:
        data = service_line_get_all_messages(line_obj)
        return data

    except Exception as e:
        return str(e)


def controller_line_get_message(line_obj, message_id):
    try:
        data = service_line_get_message(line_obj, message_id)
        return data

    except Exception as e:
        return str(e)


def controller_line_update_message(db, line_obj, message_id, json_data):
    try:
        data = service_line_update_message(db, line_obj, message_id, json_data)
        return data

    except Exception as e:
        return str(e)


def controller_line_delete_message(db, line_obj, message_id):
    try:
        data = service_line_delete_message(db, line_obj, message_id)
        return data

    except Exception as e:
        return str(e)


#########
#
# Meetup
#
#########

def controller_get_new_member_application(db, new_members_obj):
    try:
        data = service_get_new_member_application(db, new_members_obj)
        return data

    except Exception as e:
        return str(e)
