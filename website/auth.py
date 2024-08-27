from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_manager, login_user, login_required, logout_user, current_user

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        phone=request.form.get('phone')
        password=request.form.get('password')
        user=User.query.filter_by(phone=phone).first()
        if user:
            if password == user.password:
                return redirect(url_for('views.home'))
    return render_template('login.html')