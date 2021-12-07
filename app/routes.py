from app import app
from controllers import *
from app import db
from app.models import Member, Admin, LineMessage
from flask import request, send_from_directory

@app.route("/")
def index():
    return "<p>Hello World</p>"

#########
#
# Members
#
#########


@app.route("/api/members/create", methods=["POST"])
def create_member():
    data = controller_create_member(db, Member, Admin, request.json)
    return data

@app.route("/api/members/<member_id>", methods=["GET"])
def get_member(member_id):
    data = controller_get_member(Member, member_id)
    return data

@app.route("/api/members/", methods=["GET"])
def get_all_members():
    data = controller_get_all_members(Member)
    return data

#########
#
# Admin
#
#########

@app.route("/api/admins/login", methods=["POST"])
def login_admin():
    data = controller_admin_login(Admin, request.json)
    return data

@app.route("/api/admins/create", methods=["POST"])
def create_admin():
    data = controller_admin_create(Admin, request.json)
    return data

@app.route("/api/admins/delete", methods=["DELETE"])
def delete_admin():
    data = controller_admin_delete(Admin, request.json)
    return data

@app.route("/api/admins/password", methods=["POST"])
def change_admin_password():
    data = controller_admin_change_password(Admin, request.json)
    return data

#########
#
# Line
#
#########

@app.route("/api/line/messages/create", methods=["POST"])
def create_message():
    data = controller_line_create_message(LineMessage, request.json)
    return data

@app.route("/api/line/messages/send", methods=["POST"])
def send_message():
    data = controller_line_send_message(LineMessage, request.json)
    return data

@app.route("/api/line/messages/", methods=["GET"])
def get_all_messages():
    data = controller_line_get_messages(LineMessage, request.json)
    return data

@app.route("/api/line/messages/message/<message_id>", methods=["GET"])
def get_message(message_id):
    data = controller_line_get_message(LineMessage, message_id)
    return data

@app.route("/api/line/messages/message/<message_id>", methods=["POST"])
def update_message(message_id):
    data = controller_line_update_message(LineMessage, message_id, request.json)
    return data

@app.route("/api/line/messages/message/<message_id>", methods=["DELETE"])
def delete_message(message_id):
    data = controller_line_delete_message(LineMessage, message_id)
    return data


#########
#
# Meetup
#
#########

@app.route("/api/meetup/new-members", methods=["GET"])
def get_new_member_applications():
    data = controller_get_new_member_application():
    return data


