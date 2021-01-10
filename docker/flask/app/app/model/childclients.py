from app.setup import db, msmlw
from datetime import datetime

class ChildClient(db.Model):

  __tablename__ = 'childclients'

  f_index = db.Column(db.Integer, nullable=False, primary_key=True)
  f_user_id = db.Column(db.String(15), nullable=False)
  f_client_id = db.Column(db.String(15), nullable=False)
  f_child_index = db.Column(db.Integer, nullable=False)
  f_child_client_name = db.Column(db.String(255), nullable=False)
  f_manage_type = db.Column(db.String(255), nullable=False)
  f_manage_type_attr = db.Column(db.String(255), nullable=True)
  f_input_type = db.Column(db.String(255), nullable=False)
  f_input_type_attr = db.Column(db.String(255), nullable=True)
  f_created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  f_updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __repr__(self):
    return '<ChildClient %r>' % self.f_child_client_name

class ChildClientSchema(msmlw.SQLAlchemySchema):
  class Meta:
    model = ChildClient
    fields = (
      'f_index',
      'f_user_id',
      'f_client_id',
      'f_child_index',
      'f_child_client_name',
      'f_manage_type',
      'f_manage_type_attr',
      'f_input_type',
      'f_input_type_attr'
      )

class ChildClientOperater():

  def __init__(self):
    self.child_client_schema = ChildClientSchema()
    self.child_clients_schema = ChildClientSchema(many=True)

  def getChildClientList(self, client_id):
    # select * from clients;
    client_list = db.session.query(ChildClient).all()
    if client_list == None:
      return []
    else:
      return self.clients_schema.jsonify(client_list)

  def registChildClient(self, childclient):
    record = ChildClient(
      f_user_id = childclient["f_user_id"],
      f_client_id = childclient["f_client_id"],
      f_child_index = childclient["f_child_index"],
      f_child_client_name = childclient["f_child_client_name"],
      f_manage_type = childclient["f_manage_type"],
      f_manage_type_attr = childclient["f_manage_type_attr"],
      f_input_type = childclient["f_input_type"],
      f_input_type_attr = childclient["f_input_type_attr"]
    )
    # insert into clients(userid, clientname) values(...);
    db.session.add(record)
    db.session.commit()
    return self.client_schema.jsonify(record)