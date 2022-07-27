import os, secrets
from flask import current_app as app

def save_post_img(post_img):
    random_name = secrets.token_hex(8)
    _, f_ext = os.path.splitext(post_img.filename)
    post_img_name = random_name + f_ext
    post_image_path = os.path.join(app.root_path, "static\post_img" +  post_img_name)
    post_img.save(post_image_path)
    return post_img_name
