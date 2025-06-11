from app.extension import db
from datetime import datetime, UTC


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_product = db.Column(db.String(120), nullable=False)
    value = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    id_seller = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    createdAt = db.Column(db.DateTime, default=lambda: datetime.now(UTC), nullable=False)
    updatedAt = db.Column(db.DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))


    seller = db.relationship('User', backref='products')