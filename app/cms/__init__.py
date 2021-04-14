from flask import Blueprint, request

cms_bp = Blueprint(
    'cms_bp',
    __name__,
    url_prefix='/'
)


@cms_bp.route('cms', methods=['POST', 'GET'])
def cms():
    if request.method == 'POST':
        return ['You just made a post request to CMS']
    return ['You have just made a get request to CMS']
