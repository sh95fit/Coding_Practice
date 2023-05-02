from flask_restx import Namespace, Resource
from READ_GS import mysql
from flask import jsonify

ns = Namespace(
  'pw_raw',
  description='발전소 로우 데이터 조회 API'
)


@ns.route('')
class BizList(Resource) :
  def get(self) :
    try:
      cur  = mysql.connection.cursor()
      cur.execute("SELECT * FROM gsmon_business limit 1")
      results = cur.fetchone()
      cur.close()
      return jsonify(results)
    except Exception as e:
      return "Error : {}".format(e), 500

@ns.route('/<date_id>/<rtuid>')
class PWdataList(Resource) :
  def get(self, date_id, rtuid) :
    try:
      cur  = mysql.connection.cursor()
      cur.execute(f"SELECT * FROM gsmon_solar_data WHERE save_time_id = {date_id} AND rtu_id = {rtuid} limit 1")
      results = cur.fetchone()
      cur.close()
      return str(results)
    except Exception as e:
      return "Error : {}".format(e), 500
