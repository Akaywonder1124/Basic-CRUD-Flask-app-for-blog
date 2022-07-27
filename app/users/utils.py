import secrets, os
from flask import url_for, current_app as app
from flask_mail import Message
from app import mail

def save_picture(form_picture):
    random_name = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_name = random_name + f_ext
    picture_path = os.path.join(app.root_path, "static\profile_pics" +  picture_name)
    form_picture.save(picture_path)

    return picture_name

def send_reset_token(user):
    token = user.get_reset_token()
    msg = Message("Request Reset Password", sender="AOFA NAW", recipients=[user.email])
    msg.body = f"""
    Click the link below to reset your password:
    {url_for('users.reset', token=token, _external = True)}
    Do not click if you didn't make this request
    """

    mail.send(msg)