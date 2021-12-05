from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Member(db.Model):
    __tablename__ = "members"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    gender = db.Column(db.Text(1), nullable=False)
    country = db.Column(db.Text(54), nullable=False)
    native_lang = db.Column(db.Text(20), nullable=False)
    lang_focus = db.Column(db.Text(3), nullable=False)
    line_id = db.Column(db.Text(15), nullable=True)
    line_api_id = db.Column(db.String(40), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    last_modified = db.Column(db.DateTime, default=db.func.now())

    admin = db.relationship("Admin", back_populates="member", lazy=True, cascade="all, delete")

    def __repr__(self):
        return '<Member %r>' % self.first_name

class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(UUID(as_uuid=True), db.ForeignKey("members.id"), nullable=False)
    username = db.Column(db.String(65), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    member = db.relationship("Member", back_populates="admin", lazy=True, cascade="all, delete")
