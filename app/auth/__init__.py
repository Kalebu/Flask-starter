from flask import Blueprint

auth_bp = Blueprint(
    'auth_bp',
    __name__,
    url_prefix="/"
)


@auth_bp.route('signin', methods=['GET', 'POST'])
def signin():
    response = {'response': 'Signing you in'}
    return response


@auth_bp.route('signup', methods=['GET', 'POST'])
def signup():
    response = {'response': 'Signing you up'}
    return response


@auth_bp.route('signout', methods=['GET'])
def signout():
    response = {'response': 'Signing you out'}
    return response
