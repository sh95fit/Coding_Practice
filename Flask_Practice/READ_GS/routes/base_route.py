from flask import Blueprint, render_template, redirect


NAME = 'BASE'


bp = Blueprint(NAME, __name__)

@bp.route('/')
def index() :
  return 'READ GSREMS'

