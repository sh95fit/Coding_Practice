from flask import Flask, render_template


def create_app() :
  app = Flask(__name__)

  if app.config['DEBUG'] :
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

  '''ROUTE INIT'''
  from READ_GS.routes import base_route
  app.register_blueprint(base_route.bp)

  @app.errorhandler(404)
  def page_404(error) :
    return render_template('/404.html'), 404

  return app