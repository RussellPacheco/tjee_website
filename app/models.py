from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Member(db.Model):
    __tablename__ = "members"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    firstname = db.Column(db.String(35), nullable=False)
    lastname = db.Column(db.String(35), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    country = db.Column(db.String(54), nullable=False)
    native_lang = db.Column(db.String(20), nullable=False)
    lang_focus = db.Column(db.String(3), nullable=False)
    line_id = db.Column(db.String(15), nullable=True)
    line_api_id = db.Column(db.String(40), nullable=True)
    meetup_id = db.Column(db.String(10), nullable=True)
    meetup_name = db.Column(db.String(25), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    last_modified = db.Column(db.DateTime, default=db.func.now(), nullable=True)

    admin = db.relationship("Admin", back_populates="member", lazy=True, cascade="all, delete")
    messages = db.relationship("LineMessage", back_populates="member", lazy=True)

    def __repr__(self):
        return '<Member %r>' % self.firstname


class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    member_id = db.Column(UUID(as_uuid=True), db.ForeignKey("members.id"), nullable=False)
    username = db.Column(db.String(65), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    last_modified = db.Column(db.DateTime, default=db.func.now(), nullable=True)

    member = db.relationship("Member", back_populates="admin", lazy=True)

    def __repr__(self):
        return '<Admin %r>' % self.username


class LineMessage(db.Model):
    __tablename__ = "line_messages"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    created_by = db.Column(UUID(as_uuid=True), db.ForeignKey("members.id"), nullable=False)
    message = db.Column(db.String(700), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    last_sent = db.Column(db.DateTime, default=db.func.now(), nullable=True)
    last_modified = db.Column(db.DateTime, default=db.func.now(), nullable=True)

    member = db.relationship("Member", back_populates="messages", lazy=True)

    def __repr__(self):
        return '<LineMessage %r>' % self.message


class NewMembers(db.Model):
    __tablename__ = "new_members"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    meetup_id = db.Column(db.String(10), nullable=True)
    meetup_name = db.Column(db.String(25), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    def __repr__(self):
        return '<NewMember %r>' % self.meetup_name
