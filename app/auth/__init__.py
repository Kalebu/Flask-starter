from flask import Blueprint, request, redirect, url_for, render_template

auth_bp = Blueprint(
    'auth_bp',
    __name__,
    url_prefix="/",
    template_folder='templates'
)


@auth_bp.route('signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # verify login
        if True:
            return redirect(url_for('cms_bp.cms'))
    return render_template('signin.html')


@auth_bp.route('signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # verify data and add to db
        if True:
            return redirect(url_for('auth_bp.signin'))
    return render_template('signup.html')


@auth_bp.route('signout', methods=['GET'])
def signout():
    # signing out
    return redirect(url_for('home_bp.index'))
