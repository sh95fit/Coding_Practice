from flask_restx import Namespace, Resource, fields, reqparse
# from READ_GS import mysql
from flask import jsonify, Response
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.automap import automap_base
from ..db_uri import gsrems_uri


DB_URI = gsrems_uri
engine = create_engine(DB_URI)
db_session = scoped_session(sessionmaker(bind=engine))

Base = automap_base()
Base.prepare(engine, reflect=True)

gsmon_business = Base.classes.gsmon_business


ns = Namespace(
  'pw_raw',
  description='발전소 로우 데이터 조회 API'
)


biz_model = ns.model('gsmon_business', {
  'id' : fields.Integer(required=True, description='사업 ID'),
  'energe': fields.String(required=True, description='에너지원'),
  'cat1' : fields.String(required=True, description='카테고리1'),
  'name' : fields.String(required=True, description='사업명')
})


@ns.route('/businesses')
class BizList(Resource) :
  @ns.marshal_list_with(biz_model)
  def get(self) :
    data = db_session.query(gsmon_business).all()
    return data