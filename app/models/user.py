from enum import Enum
from datetime import datetime, UTC
from app.extension import db
from passlib.hash import bcrypt

class RoleEnum(Enum):
    SELLER = "SELLER"
    BUYER = "BUYER"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum(RoleEnum), default=RoleEnum.SELLER, nullable=False)
    createdAt = db.Column(db.DateTime, default=lambda: datetime.now(UTC), nullable=False)

    def set_password(self, password):
        self.password = bcrypt.hash(password)

    def check_password(self, password):
        return bcrypt.verify(password, self.password)