from app import app
from controllers import *
from app import db
from app.models import Member, Admin
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

@app.route("/api/members/<id>")
def get_member(id):
    data = controller_get_member(Member, id)
    return data

@app.route("/api/members/")
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

@app.route("/api/admins/delete", methods=["POST"])
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

