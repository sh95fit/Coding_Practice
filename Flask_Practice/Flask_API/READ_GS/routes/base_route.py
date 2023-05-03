from flask import Blueprint, render_template, redirect, request
import requests


NAME = 'BASE'


bp = Blueprint(NAME, __name__)

@bp.route('/')
def index() :
  return 'READ GSREMS'

@bp.route('/rawdata', methods=['GET'])
def rawdata() :
  rtu_id = request.args.get('rtu_id')
  date_id = request.args.get('date_id')

  # API 호출
  url = f"http://127.0.0.1:5000/api/pw_raw/{rtu_id}/{date_id}"
  response = requests.get(url)
  if response.ok :
    data = response.json()
  else :
    data = None
  # data = requests.get(url)
  return render_template('index.html', data=data)