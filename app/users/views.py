from flask import Blueprint, render_template, redirect, flash, url_for, request
from .utils import save_picture, send_reset_token
from flask_login import current_user, login_required, logout_user, login_user
from app import db, bcrypt
from ..model import User
from .forms import (RegistrationForm, RequestResetPassword, 
                    ResetPassword, LoginForm, UpdateAccountForm)

users = Blueprint("users", __name__)


@users.route("/register", methods = ["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data, email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for("main.index"))
    return render_template("register.html", title="Register", form=form)

@users.route("/login", methods = ["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page) 
            else:
                return redirect(url_for("main.index"))
        else:
            flash ("Login unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)


@users.route("/logout", methods = ["POST", "GET"])
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@users.route("/account", methods = ["POST", "GET"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated Successfully", "success")
        return redirect(url_for('users.account'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics' + current_user.image_file)
    return render_template("account.html", form=form, image_file=image_file)


@users.route("/request_reset", methods = ["POST", "GET"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RequestResetPassword()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_token(user)
        flash(f"Password reset token sent", "info")
        return redirect(url_for('users.login'))
    return render_template("request_reset.html", form=form)

@users.route("/reset/<token>", methods = ["POST", "GET"])
def reset(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_token(token)
    if user is None:
        flash(f"Invalid or Expired token", "warning")
        return redirect(url_for('users.reset_request'))
    form = ResetPassword()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user.password = hashed_password
        db.session.commit()
        flash(f"Password reset successfully. Please Login", "success")
        return redirect(url_for("users.login"))
    return render_template('reset.html', form=form)

