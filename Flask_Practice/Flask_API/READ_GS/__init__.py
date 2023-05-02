from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mysqldb import MySQL
from .db_uri import gsrems_uri, mysql_ip, mysql_user, mysql_pw, mysql_db, mysql_port


# db = SQLAlchemy()
# migrate = Migrate()
mysql = MySQL()


def create_app() :
  app = Flask(__name__)

  app.config['SECRET_KEY'] = 'GSremsTEST'
  app.config['SESSION_COOKIE_NAME'] = 'READ_GS'

  app.config['MYSQL_HOST'] = mysql_ip
  app.config['MYSQL_USER'] = mysql_user
  app.config['MYSQL_PASSWORD'] = mysql_pw
  app.config['MYSQL_DB'] = mysql_db
  app.config['MYSQL_PORT'] = mysql_port
  app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
  app.config['MYSQL_CONNECT_TIMEOUT'] = 100
  app.config['MYSQL_DATABASE_CHARSET'] = 'utf8'

  # app.config['SQLALCHEMY_DATABASE_URI'] = gsrems_uri
  # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  if app.config['DEBUG'] :
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

  '''DB INIT'''
  # db.init_app(app)
  # if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
  #   migrate.init_app(app, db, render_as_batch=True)
  # else :
  #   migrate.init_app(app, db)

  mysql = MySQL(app)
  mysql.init_app(app)


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