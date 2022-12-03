from product import app,db
from flask import render_template,request,redirect,url_for,flash
from product import User

@app.route('/')
@app.route('home')
def home_page():
    return render_template('home.html')

@app.route('/login', methods=['GET', POST])
def login_page():
    form=login_page()
    if form.validate_on_login():
        attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
        if attempted_user and attempted_user.check_password_hash_correction(
            attempted_user=form.password_hash.data
        ):
            login_user(attempted_user)
            flash (f'Vi ste logovani kao: {attempted_user.email_address}', category='success')
            return redirect(url_for('home_page', category='danger'))
        else:
            flash(f'Pogresan e-mail ili pasvord')
            return render_template('login.html')

        @app.route('logout.html')
        def logout_page():
             logout_user()
        flash ('Are you sure you want to log out from the console', category='info')

        @app.route('thumbnail.html')
        def thumbnail ():
            image_file= url_for('static',filename='backgrounds/'+ current.user.image_file)
            return render_template('thumbnail.html',title='thumbnail')

@app.route('/go_outside_flask')
def go_outside_flask_method():
    return redirect("https://www.tech387.com/product-arena/full-stack-developer", code=302)
