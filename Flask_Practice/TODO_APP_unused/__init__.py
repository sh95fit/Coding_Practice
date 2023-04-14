from flask import Flask
# app = Flask(__name__)
app = Flask('TODO_APP')
app = Flask(__name__.split('.')[0])
