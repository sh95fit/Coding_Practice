from flask_restx import Namespace, Resource, fields, reqparse
# from READ_GS import mysql
from flask import jsonify, Response
import json

from sqlalchemy import create_engine, and_
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
  @ns.marshal_list_with(biz_model, skip_none=True)
  def get(self) :
    data = db_session.query(gsmon_business).all()
    return data



gsmon_solar_data = Base.classes.gsmon_solar_data

rawdata_model = ns.model('gsmon_solar_data', {
  'id' : fields.Integer(required=True, description='사업 ID'),
  'rtu_id' : fields.Integer(required=True, description='RTU_ID'),
  'inverter_id' : fields.Integer(required=True, description='인버터 ID'),
  'multi' : fields.Integer(required=True, description='멀티'),
  'phase' : fields.Integer(required=True, description='상 구분'),
  'code' : fields.Integer(required=True, description='국번'),
  'lerr' : fields.Integer(required=True, description='에러코드'),
  'inv' : fields.Float(required=True, description='PV전압1'),
  'inv2' : fields.Float(required=True, description='PV전압2'),
  'inv3' : fields.Float(required=True, description='PV전압3'),
  'inv4' : fields.Float(required=True, description='PV전압4'),
  'inv5' : fields.Float(required=True, description='PV전압5'),
  'inv6' : fields.Float(required=True, description='PV전압6'),
  'ina' : fields.Float(required=True, description='PV전류1'),
  'ina2' : fields.Float(required=True, description='PV전류2'),
  'ina3' : fields.Float(required=True, description='PV전류3'),
  'ina4' : fields.Float(required=True, description='PV전류4'),
  'ina5' : fields.Float(required=True, description='PV전류5'),
  'ina6' : fields.Float(required=True, description='PV전류6'),
  'inp' : fields.Float(required=True, description='PV전압'),
  'outv' : fields.Float(required=True, description='출력 전압'),
  'outa' : fields.Float(required=True, description='출력 전류'),
  'outvr' : fields.Float(required=True, description='s상 전압'),
  'outvs' : fields.Float(required=True, description='v상 전압'),
  'outvt' : fields.Float(required=True, description='t상 전압'),
  'outar' : fields.Float(required=True, description='s상 전류'),
  'outas' : fields.Float(required=True, description='v상 전류'),
  'outat' : fields.Float(required=True, description='t상 전류'),
  'outp' : fields.Float(required=True, description='출력 전력'),
  'pf' : fields.Float(required=True, description='역률'),
  'frq' : fields.Float(required=True, description='주파수'),
  'temp' : fields.Float(required=True, description='온도'),
  'tpg' : fields.Float(required=True, description='금일발전량'),
  'cpg' : fields.Float(required=True, description='누적발전량'),
  'save_time_id' : fields.Float(required=True, description='저장시간 ID'),
  'save_time' : fields.DateTime(required=True, description='저장시간')
})


@ns.route('/<int:rtu_id>/<int:date_id>')
class RawData(Resource) :
  @ns.marshal_list_with(rawdata_model, skip_none=True)
  def get(self, rtu_id, date_id) :
    data = db_session.query(gsmon_solar_data).filter(and_(gsmon_solar_data.rtu_id==rtu_id, gsmon_solar_data.save_time_id==date_id)).all()
    return data