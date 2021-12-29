#########
#
# Members
#
#########

def dao_create_member(db, member_obj, firstname, lastname, gender, country, native_lang, lang_focus, line_id,
                      line_api_id, meetup_id, meetup_name):
    new_member = member_obj(firstname=firstname, lastname=lastname, gender=gender, country=country,
                            native_lang=native_lang, lang_focus=lang_focus, line_id=line_id,
                            line_api_id=line_api_id, meetup_id=meetup_id, meetup_name=meetup_name)
    db.session.add(new_member)
    db.session.commit()


def dao_get_member_by_fullname(member_obj, firstname, lastname):
    result = member_obj.query.filter_by(firstname=firstname, lastname=lastname).first()
    return result


def dao_get_member_by_id(member_obj, member_id):
    result = member_obj.query.filter_by(id=member_id).first()
    return result


def dao_get_all_members(member_obj):
    results = member_obj.query.all()
    return results


#########
#
# Admin
#
#########

def dao_get_admin_by_username(admin_obj, username):
    result = admin_obj.query.filter_by(username=username).first()
    return result


def dao_create_admin(db, admin_obj, member_id, username, password):
    new_admin = admin_obj(member_id=member_id, username=username, password=password)
    db.session.add(new_admin)
    db.session.commit()


def dao_admin_delete(db, admin_obj, username):
    admin = admin_obj.query.filter_by(username=username).first()
    db.session.delete(admin)
    db.session.commit()


def dao_admin_change_password(db, admin_obj, username, password):
    admin = admin_obj.query.filter_by(username=username).first()
    admin.password = password
    db.session.commit()


#########
#
# Line
#
#########

def dao_line_save_webhook(db, webhook_obj, line_type, timestamp, userId=None, groupId=None, message=None):
    print("in dao_line_save_webhook")
    if line_type in ["leave", "memberJoined", "memberLeft"]:
        print("in if statement for dao")
        new_webhook = webhook_obj(type=line_type, timestamp=timestamp, groupId=groupId, userId=userId)
        db.session.add(new_webhook)
        db.session.commit()

    elif line_type in ["follow", "unfollow"]:
        new_webhook = webhook_obj(type=line_type, timestamp=timestamp, userId=userId)
        db.session.add(new_webhook)
        db.session.commit()

    elif line_type == "message":
        new_message = webhook_obj(type=line_type, timestamp=timestamp, userId=userId, message=message)
        db.session.add(new_message)
        db.session.commit()


def dao_line_get_webhook(webhook_obj, userId=None, groupId=None, line_type=None):

    if line_type in ["leave", "memberJoined", "memberLeft"]:
        result = webhook_obj.query.filter_by(type=line_type, groupId=groupId).order_by(webhook_obj.timestamp).first()
        return result

    elif line_type in ["follow", "unfollow", "message"]:

        result = webhook_obj.query.filter_by(type=line_type, userId=userId).first()

        return result


def dao_line_get_bot_permission(bot_permission_obj, permission_name):
    result = bot_permission_obj.query.filter_by(permission_name=permission_name).first()
    return result


def dao_line_get_all_bot_permissions(bot_permission_obj):
    result = bot_permission_obj.query.all()
    return result


def dao_line_change_bot_permission(db, bot_permission_obj, permission_name, permission_value, last_modified):
    bot_permission_obj.query.filter_by(permission_name=permission_name).update(dict(permission_value=permission_value, last_modified=last_modified))
    db.session.commit()


def dao_line_create_message(db, line_obj, created_by, message):
    new_message = line_obj(created_by=created_by, message=message)
    db.session.add(new_message)
    db.session.commit()


def dao_line_get_all_messages(line_obj):
    results = line_obj.query.all()
    return results


def dao_line_get_message(line_obj, message_id):
    result = line_obj.query.filter_by(id=message_id).first()
    return result


def dao_line_update_message(db, line_obj, message_id, new_message, last_modified):
    line_obj.query.filter_by(id=message_id).update(dict(message=new_message, last_modified=last_modified))
    db.session.commit()


def dao_line_update_message_time(db, line_obj, message_id, last_modified):
    line_obj.query.filter_by(id=message_id).update(dict(last_modified=last_modified))
    db.session.commit()


def dao_line_delete_message(db, line_obj, message_id):
    message = line_obj.query.filter_by(id=message_id).first()
    db.session.delete(message)
    db.session.commit()


#########
#
# Meetup
#
#########

def dao_get_all_new_members(new_members_obj):
    results = new_members_obj.query.all()
    return results
