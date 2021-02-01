from app import db


class Item(db.Model):
    id = db.Column(db.Integer, Primary_key=True, sqlite_autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    value = db.column(db.Integer, default=0)
    status = db.column(db.Integer, default=0)
