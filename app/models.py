from exts import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)


class OrderModel(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(200), nullable=False)
    user_mobile = db.Column(db.Integer, nullable=False)
    user_state = db.Column(db.varchar(10), nullable=False)
    user_city = db.Column(db.varchar(10), nullable=False)
    user_district = db.Column(db.varchar(20), nullable=False)
    user_address = db.Column(db.varchar(200), nullable=False)
    order_type = db.Column(db.String(200), nullable=False)
    visit_time = db.Column(db.DateTime, nullable=False)
    book_number = db.Column(db.Integer)
    make_time = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.relationship("UserModel", backref=db.backref("orders"),order_by=make_time.desc())





# db.drop_all()#clear all table
# db.create_all()#create user table