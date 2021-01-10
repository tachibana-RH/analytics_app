from app.setup import db, msmlw
from datetime import datetime

class User(db.Model):

  __tablename__ = 'users'

  f_user_id = db.Column(db.String(15), nullable=False, primary_key=True)
  f_user_name = db.Column(db.String(255), nullable=False)
  f_password = db.Column(db.String(255), nullable=False)
  f_created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  f_updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __repr__(self):
    return '<User %r>' % self.f_user_name

class UserSchema(msmlw.SQLAlchemySchema):
  class Meta:
    model = User
    fields = ('f_user_id', 'f_user_name', 'f_password')

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
    result = db.session.query(User).filter_by(f_user_name=user['f_user_name']).first()
    if result == None:
      return []
    else:
      return self.user_schema.jsonify(result).json

  def getUserFromID(self, _Id):
    result = db.session.query(User).filter_by(f_user_id=_Id).first()
    if result == None:
      return []
    else:
      return self.user_schema.jsonify(result).json

  def isExistUser(self, _user):
    # select * from users where name=${user.name}
    result = db.session.query(User).filter_by(f_user_name=_user['f_user_name']).first()
    if result == None:
      return False
    else:
      return True

  def isUnAuthUser(self, user):
    # select * from users where name=${user.name} password=${user.password}
    result = db.session.query(User).filter_by(
      f_user_name=user['f_user_name'], f_password=user['f_password']).first()
    if result == None:
      return True
    else:
      return False

  def registUser(self, user):
    record = User(
      f_user_name = user['f_user_name'],
      f_password = user['f_password']
    )
    # insert into users(name, password) values(...)
    db.session.add(record)
    db.session.commit()
    return self.user_schema.jsonify(record)