from flask import Blueprint, request
from flask.templating import render_template

cms_bp = Blueprint(
    'cms_bp',
    __name__,
    url_prefix='/',
    template_folder='templates'
)


@cms_bp.route('cms', methods=['POST', 'GET'])
def cms():
    if request.method == 'POST':
        # do something
        pass
    return render_template('cms.html')
