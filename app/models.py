from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Member(db.Model):
    __tablename__ = "members"
    id = db.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    firstname = db.Column("firstname", db.String(35), nullable=False)
    lastname = db.Column("lastname", db.String(35), nullable=False)
    gender = db.Column("gender", db.String(1), nullable=False)
    country = db.Column("country", db.String(54), nullable=False)
    native_lang = db.Column("native_lang", db.String(20), nullable=False)
    lang_focus = db.Column("lang_focus", db.String(3), nullable=False)
    line_id = db.Column("line_id", db.String(15), nullable=True, unique=True)
    line_api_id = db.Column("line_api_id", db.String(40), nullable=True, unique=True)
    meetup_id = db.Column("meetup_id", db.String(10), nullable=True, unique=True)
    meetup_name = db.Column("meetup_name", db.String(25), nullable=True)
    created_at = db.Column("created_at", db.DateTime, default=db.func.now(), nullable=False)
    last_modified = db.Column("last_modified", db.DateTime, default=db.func.now(), nullable=True)

    admin = db.relationship("Admin", back_populates="member", lazy=True, cascade="all, delete")
    messages = db.relationship("LineMessage", back_populates="member", lazy=True)

    def __repr__(self):
        return '<Member %r>' % self.firstname


class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    member_id = db.Column("member_id", UUID(as_uuid=True), db.ForeignKey("members.id", ondelete="CASCADE"), nullable=False, unique=True)
    username = db.Column("username", db.String(65), unique=True, nullable=False)
    password = db.Column("password", db.String(200), unique=True, nullable=False)
    created_at = db.Column("created_at", db.DateTime, default=db.func.now(), nullable=False)
    last_modified = db.Column("last_modified", db.DateTime, default=db.func.now(), nullable=True)
    member = db.relationship("Member", back_populates="admin", lazy=True)

    def __repr__(self):
        return '<Admin %r>' % self.username


class LineMessage(db.Model):
    __tablename__ = "line_messages"
    id = db.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    created_by = db.Column("created_by", UUID(as_uuid=True), db.ForeignKey("members.id", ondelete="SET NULL"), nullable=False)
    message = db.Column("message", db.String(700), nullable=False)
    created_at = db.Column("created_at", db.DateTime, default=db.func.now(), nullable=False)
    last_sent = db.Column("last_sent", db.DateTime, default=db.func.now(), nullable=True)
    last_modified = db.Column("last_modified", db.DateTime, default=db.func.now(), nullable=True)

    member = db.relationship("Member", back_populates="messages", lazy=True)

    def __repr__(self):
        return '<LineMessage %r>' % self.message


class NewMembers(db.Model):
    __tablename__ = "new_members"
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    meetup_id = db.Column("meetup_id", db.String(10), nullable=True, unique=True)
    meetup_name = db.Column("meetup_name", db.String(25), nullable=True)
    created_at = db.Column("created_at", db.DateTime, default=db.func.now(), nullable=False)

    def __repr__(self):
        return '<NewMember %r>' % self.meetup_name


class LineWebhooks(db.Model):
    __tablename__ = "line_webhooks"
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    type = db.Column("type", db.String(14), nullable=False)
    userId = db.Column("userId", db.String(40), nullable=True)
    timestamp = db.Column("timestamp", db.DateTime, nullable=False)
    groupId = db.Column("groupId", db.String(40), nullable=True)
    message = db.Column("message", db.String(200), nullable=True)

    def __repr__(self):
        return '<LineWebhook %r>' % self.type


class BotPermissions(db.Model):
    __tablename__ = "bot_permissions"
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    permission_name = db.Column("permission_name", db.String(15), nullable=False)
    permission_value = db.Column("permission_value", db.Boolean, nullable=False)
    last_modified = db.Column("last_modified", db.DateTime, default=db.func.now(), nullable=True)

    def __repr__(self):
        return '<BotPermission %r>' %self.permission_name


