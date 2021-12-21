from app import app
from controllers import *
from app import db
from app.models import Member, Admin, LineMessage, NewMembers, LineWebhooks
from flask import request, Response


@app.route("/")
def index():
    return "<p>Hello World</p>"

#########
#
# Members
#
#########


@app.route("/api/members/create/", methods=["POST"])
def member_create():
    data = controller_create_member(db, Member, request.json)
    return data


@app.route("/api/members/<member_id>/", methods=["GET"])
def member_get(member_id):
    data = controller_get_member(Member, member_id)
    return data


@app.route("/api/members/", methods=["GET"])
def member_get_all():
    data = controller_get_all_members(Member)
    return data


#########
#
# Admin
#
#########

@app.route("/api/admins/login/", methods=["POST"])
def admin_login():
    data = controller_admin_login(Admin, request.json)
    return data


@app.route("/api/admins/create/", methods=["POST"])
def admin_create():
    data = controller_admin_create(db, Admin, request.json)
    return data


@app.route("/api/admins/delete/", methods=["DELETE"])
def admin_delete():
    data = controller_admin_delete(db, Admin, request.json)
    return data


@app.route("/api/admins/password/", methods=["POST"])
def admin_change_password():
    data = controller_admin_change_password(db, Admin, request.json)
    return data


#########
#
# Line
#
#########

@app.route("/api/line/", methods=["POST"])
def webhook():
    data = controller_line_webhook(db, LineWebhooks, request.headers, request.body, request.json)
    # data = controller_line_webhook(db, LineWebhooks, request.json)
    return data


@app.route("/api/line/messages/create/", methods=["POST"])
def message_create():
    data = controller_line_create_message(db, LineMessage, request.json)
    return data


@app.route("/api/line/messages/send/", methods=["POST"])
def message_send():
    data = controller_line_send_message(db, LineMessage, request.json)
    return data


@app.route("/api/line/messages/", methods=["GET"])
def message_get_all():
    data = controller_line_get_all_messages(LineMessage)
    return data


@app.route("/api/line/messages/message/<message_id>/", methods=["GET"])
def message_get(message_id):
    data = controller_line_get_message(LineMessage, message_id)
    return data


@app.route("/api/line/messages/message/<message_id>/", methods=["POST"])
def message_update(message_id):
    data = controller_line_update_message(db, LineMessage, message_id, request.json)
    return data


@app.route("/api/line/messages/message/<message_id>/", methods=["DELETE"])
def message_delete(message_id):
    data = controller_line_delete_message(db, LineMessage, message_id)
    return data


#########
#
# Meetup
#
#########

@app.route("/api/meetup/new-members/", methods=["GET"])
def get_new_member_applications():
    data = controller_get_new_member_application(db, NewMembers)
    return data
