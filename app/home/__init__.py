from flask import Blueprint
from flask.templating import render_template

home_bp = Blueprint(
    'home_bp',
    __name__,
    url_prefix='/',
    template_folder='templates'
)


@home_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')
