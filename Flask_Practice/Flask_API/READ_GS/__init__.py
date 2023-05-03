from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mysqldb import MySQL
from .db_uri import gsrems_uri


def create_app() :
  app = Flask(__name__)

  app.config['SECRET_KEY'] = 'GSremsTEST'
  app.config['SESSION_COOKIE_NAME'] = 'READ_GS'


  if app.config['DEBUG'] :
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


  '''ROUTE INIT'''
  from READ_GS.routes import base_route
  app.register_blueprint(base_route.bp)


  '''RESTX INIT'''
  from READ_GS.apis import blueprint as api
  app.register_blueprint(api)

  app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'


  @app.errorhandler(404)
  def page_404(error) :
    return render_template('/404.html'), 404


  return app