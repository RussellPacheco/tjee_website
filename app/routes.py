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


@app.route("/api/member/create", methods=["POST"])
def createmember():
    data = controller_create_member(db, Member, Admin, request.json)
    return data

@app.route("/api/member/<id>")
def getmember(id):
    data = controller_get_user(Member, id)
    return data


#########
#
# Admin
#
#########

@app.route("/api/admin/login", methods=["POST"])
def loginadmin():
    data = controller_login_admin(Admin, request.json)
    return data