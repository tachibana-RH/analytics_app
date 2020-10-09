from app.setup import db, msmlw
from datetime import datetime

class User(db.Model):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  password = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __repr__(self):
    return '<User %r>' % self.name

class UserSchema(msmlw.SQLAlchemySchema):
  class Meta:
    model = User
    fields = ('id', 'name', 'password')

class UserOperater():

  def __init__(self):
    self.user_schema = UserSchema()
    self.users_schema = UserSchema(many=True)

  def getUserList(self):
    # select * from users
    user_list = db.session.query(User).all()
    if user_list == None:
      return []
    else:
      return self.user_schema.jsonify(user_list)

  def getUser(self, user):
    # select * from users where name=${user.name}
    result = db.session.query(User).filter_by(name=user['name']).first()
    if result == None:
      return []
    else:
      return self.user_schema.jsonify(result).json

  def getUserFromID(self, aId):
    result = db.session.query(User).filter_by(id=aId).first()
    if result == None:
      return []
    else:
      return self.user_schema.jsonify(result).json

  def isExistUser(self, user):
    # select * from users where name=${user.name}
    result = db.session.query(User).filter_by(name=user['name']).first()
    if result == None:
      return False
    else:
      return True

  def isUnAuthUser(self, user):
    # select * from users where name=${user.name} password=${user.password}
    result = db.session.query(User).filter_by(
      name=user['name'], password=user['password']).first()
    if result == None:
      return True
    else:
      return False

  def registUser(self, user):
    record = User(
      name = user['name'],
      password = user['password']
    )
    # insert into users(name, password) values(...)
    db.session.add(record)
    db.session.commit()
    return self.user_schema.jsonify(record)