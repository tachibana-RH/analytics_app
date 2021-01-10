from app.setup import db, msmlw
from datetime import datetime

class Client(db.Model):

  __tablename__ = 'clients'

  f_client_id = db.Column(db.String(15), nullable=False, primary_key=True)
  f_user_id = db.Column(db.String(15), nullable=False)
  f_client_name = db.Column(db.String(255), nullable=False)
  f_category = db.Column(db.String(255), nullable=False)
  f_client_origin = db.Column(db.String(255), nullable=False)
  f_created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  f_updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __repr__(self):
    return '<Client %r>' % self.f_client_name

class ClientSchema(msmlw.SQLAlchemySchema):
  class Meta:
    model = Client
    fields = (
      'f_client_id',
      'f_user_id',
      'f_client_name',
      'f_category',
      'f_client_origin'
    )

class ClientOperater():

  def __init__(self):
    self.client_schema = ClientSchema()
    self.clients_schema = ClientSchema(many=True)

  def getClientList(self, userid):
    # select * from clients where f_user_id = userid;
    client_list = db.session.query(Client)\
                    .filter(Client.f_user_id==userid)\
                    .all()
    if client_list == None:
      return []
    else:
      return self.client_schema.jsonify(client_list)

  def registClient(self, client):
    record = Client(
      f_user_id = client['f_user_id'],
      f_client_name = client['f_client_name'],
      f_category = client['f_category'],
      f_client_origin = client['f_client_origin'],
    )
    # insert into clients(userid, clientname, f_category, f_client_origin) values(...);
    db.session.add(record)
    db.session.commit()
    return self.user_schema.jsonify(record)