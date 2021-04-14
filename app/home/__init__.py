from flask import Blueprint

home_bp = Blueprint(
    'home_bp',
    __name__,
    url_prefix='/'
)


@home_bp.route('/', methods=['GET'])
def index():
    return ['You Finally home']
