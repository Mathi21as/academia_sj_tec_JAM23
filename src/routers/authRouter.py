from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager , login_user, logout_user, login_required
from models.ModelUser import ModelUser
from models.entities.User import User
from app import db

authRouter = Blueprint("authRouter", __name__)

@authRouter.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':        
        user = User( 0 , None, None, None, None, request.form['email'], request.form['password'] )
        loguedUser = ModelUser.login(db, user)

        if loguedUser != None:
            if loguedUser.password:
                login_user(loguedUser)
                return redirect(url_for('home'))
            else:
                flash("Credenciales erroneas")
                return render_template('auth/login.html')
        else:
            flash("Credenciales erroneas")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

