from app import app
from controllers import *
from app import db
from app.models import Member, Admin, LineMessage, NewMembers, LineWebhooks, BotPermissions
from flask import request, render_template
from functools import wraps


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '')

        invalid_msg = {
            'message': 'Invalid token. Registration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers.split(".")) != 3:
            return jsonify(invalid_msg), 401

        try:
            data = jwt.decode(auth_headers, current_app.config['SECRET_KEY'], algorithms="HS256")
            user = Admin.query.filter_by(username=data['sub']).first()
            if not user:
                raise RuntimeError('Admin not found')
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
        except jwt.InvalidTokenError:
            return jsonify(invalid_msg), 401

    return _verify


@app.route("/")
def index():
    return render_template("index.html")


#########
#
# Members
#
#########


@app.route("/api/members/create/", methods=["POST"])
@token_required
def member_create():
    data = controller_create_member(db, Member, request.get_json())
    return data


@app.route("/api/members/<member_id>/", methods=["GET"])
@token_required
def member_get(member_id):
    data = controller_get_member(Member, member_id)
    return data


@app.route("/api/members/", methods=["GET"])
@token_required
def member_get_all():
    data = controller_get_all_members(Member)
    return data

@app.route("/api/members/update/", methods=["POST"])
@token_required
def member_update():
    data = controller_member_update(db, Member, request.get_json())
    return data

#########
#
# Admin
#
#########

@app.route("/api/admins/login/", methods=["POST"])
def admin_login():
    data = controller_admin_login(Admin, request.get_json())
    return data


@app.route("/api/admins", methods=["GET"])
@token_required
def admin_get_all():
    data = controller_admin_get_all(Admin)
    return data


@app.route("/api/admins/create/", methods=["POST"])
@token_required
def admin_create():
    data = controller_admin_create(db, Admin, request.get_json())
    return data

@app.route("/api/admins/delete/", methods=["DELETE"])
@token_required
def admin_delete():
    data = controller_admin_delete(db, Admin, request.get_json())
    return data


@app.route("/api/admins/password/", methods=["POST"])
@token_required
def admin_change_password():
    data = controller_admin_change_password(db, Admin, request.get_json())
    return data


#########
#
# Line
#
#########

@app.route("/api/line/", methods=["POST"])
@token_required
def webhook():
    data = controller_line_webhook(db=db,
                                   webhook_obj=LineWebhooks,
                                   bot_permission_obj=BotPermissions,
                                   body=request.get_data(as_text=True),
                                   headers=request.headers,
                                   json_data=request.get_json())
    # data = controller_line_webhook(db, LineWebhooks, request.get_json())
    return data


@app.route("/api/line/bot/", methods=["POST"])
@token_required
def change_bot_permissions():
    data = controller_line_change_bot_permission(db, BotPermissions, request.get_json())
    return data


@app.route("/api/line/bot/", methods=["GET"])
@token_required
def get_bot_permissions():
    data = controller_line_get_bot_permissions(BotPermissions)
    return data


@app.route("/api/line/messages/create/", methods=["POST"])
@token_required
def message_create():
    data = controller_line_create_message(db, LineMessage, request.get_json())
    return data


@app.route("/api/line/messages/send/", methods=["POST"])
@token_required
def message_send():
    data = controller_line_send_message(db, LineMessage, request.get_json())
    return data


@app.route("/api/line/messages/", methods=["GET"])
@token_required
def message_get_all():
    data = controller_line_get_all_messages(LineMessage)
    return data


@app.route("/api/line/messages/message/<message_id>/", methods=["GET"])
@token_required
def message_get(message_id):
    data = controller_line_get_message(LineMessage, message_id)
    return data


@app.route("/api/line/messages/message/<message_id>/", methods=["POST"])
@token_required
def message_update(message_id):
    data = controller_line_update_message(db, LineMessage, message_id, request.get_json())
    return data


@app.route("/api/line/messages/message/<message_id>/", methods=["DELETE"])
@token_required
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
    data = controller_get_new_member_applications(NewMembers)
    return data


@app.route("/api/meetup/new-members/update", methods=["GET"])
def update_new_member_applications():
    data = controller_update_new_member_applications()
    return data


@app.route("/api/meetup/new-members/approve", methods=["POST"])
def approve_new_member():
    data = controller_approve_new_member(db, NewMembers, request.get_json())
    return data


@app.route("/api/meetup/new-members/deny", methods=["POST"])
def deny_new_member():
    data = controller_deny_new_member(db, NewMembers, request.get_json())
    return data


@app.route("/api/meetup/current-members", methods=["GET"])
@token_required
def meetup_get_current_members():
    data = controller_get_current_members(Member)
    return data


@app.route("/api/meetup/events", methods=["GET"])
def meetup_get_current_events():
    data = controller_get_current_events()
    return data
