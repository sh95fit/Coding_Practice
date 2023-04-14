from flask import Flask
from flask import render_template
from flask import jsonify

from dotenv import load_dotenv


from flask_sqlalchemy import SQLAlchemy
from .config import Config
# from .models import models        # 순환참조 에러 발생

load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


@app.route('/')
def index():
    # from .models import models
    # tasks = models.Task.query.all()
    return render_template('index.html')
    # return jsonify(tasks)     # db 인식 에러 발생


if __name__ == '__main__':
    app.run()
