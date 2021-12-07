from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Member(db.Model):
    __tablename__ = "members"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    gender = db.Column(db.Text(1), nullable=False)
    country = db.Column(db.Text(54), nullable=False)
    native_lang = db.Column(db.Text(20), nullable=False)
    lang_focus = db.Column(db.Text(3), nullable=False)
    line_id = db.Column(db.Text(15), nullable=True)
    line_api_id = db.Column(db.String(40), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    last_modified = db.Column(db.DateTime, default=db.func.now(), nullable=True)

    admin = db.relationship("Admin", back_populates="member", lazy=True, cascade="all, delete")
    messages = db.relationship("Line_Message", back_populates="member", lazy=True)

    def __repr__(self):
        return '<Member %r>' % self.first_name


class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    member_id = db.Column(UUID(as_uuid=True), db.ForeignKey("members.id"), nullable=False)
    username = db.Column(db.String(65), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    last_modified = db.Column(db.DateTime, default=db.func.now(), nullable=True)

    member = db.relationship("Member", back_populates="admin", lazy=True, cascade="all, delete")

    def __repr__(self):
        return '<Admin %r>' % self.username


class Line_Message(db.Model):
    __tablename__ = "line_messages"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    created_by = db.Column(UUID(as_uuid=True), db.ForeignKey("members.id"), nullable=False)
    message = db.Column(db.Text(700), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    last_sent = db.Column(db.DateTime, default=db.func.now(), nullable=True)
    last_modified = db.Column(db.DateTime, default=db.func.now(), nullable=True)

    member = db.relationship("Member", back_populates="messages", lazy=True)

    def __repr__(self):
        return '<Line_Message %r>' % self.message