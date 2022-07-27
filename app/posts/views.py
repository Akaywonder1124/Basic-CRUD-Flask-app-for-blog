from flask import Blueprint, render_template, redirect, request, url_for, flash, abort
from app import db
from flask_login import login_required, current_user
from sqlalchemy import desc
from .forms import PostForm, UpdatePostForm 
from ..model import Post, User
from .utils import save_post_img

posts = Blueprint("posts", __name__)


@posts.route("/post", methods = ["POST", "GET"])
@login_required
def post():
    form = PostForm()
    if request.method =="POST":
        if form.validate_on_submit():
            if form.post_img.data:
                post_img_file = save_post_img(form.post_img.data)
            post = Post(title = form.title.data,
                         content= form.content.data,
                        author = current_user,
                        featured_image = post_img_file,
                        categories=form.categories.data)
            db.session.add(post)
            db.session.commit()
            flash("Post Created successfully", "success")
        return redirect(url_for("main.index"))
    elif request.method == "GET":
        return render_template("create_post.html", form=form , title="Create Post", legend ="Create Post")

@posts.route("/blog/<int:post_id>")
def blog(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("blog.html", post=post)

@posts.route("/blog/<int:post_id>/update", methods = ["POST", "GET"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = UpdatePostForm()
    if form.validate_on_submit():
        if form.title.data:
            post.title = form.title.data
        if form.content.data:
            post.content = form.content.data
        if form.categories.data:
            post.categories = form.categories.data
        if form.post_img.data:
            post_img_file = save_post_img(form.post_img.data)
            post.featured_image = post_img_file
        db.session.commit()
        flash("Your post has been Updated", "success")
        return redirect(url_for("posts.blog", post_id = post.id))
    form.title.data = post.title
    form.content.data = post.content
    return render_template("update_post.html", form=form, title="Update Post", legend ="Update Post")

@posts.route("/blog/<int:post_id>/delete", methods = ["POST", "GET"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted", "success")
    return redirect(url_for("main.index"))


@posts.route("/user/<string:username>")
def user_post(username):
    user = User.query.filter_by(username = username).first_or_404()
    page = request.args.get("page", 1, type=int)
    post = db.session.query(Post).filter_by(author=user)\
                                .order_by(desc(Post.id))\
                                .paginate(page=page, per_page=6)
    return render_template("user_posts.html", post = post, user=user)

@posts.route("/categories/<string:categories>")
def categories_post(categories):
    page = request.args.get("page", 1, type=int)
    post = db.session.query(Post).filter_by(categories = categories)\
                                .order_by(desc(Post.id))\
                                .paginate(page=page, per_page=6)
    return render_template("categories_post.html", post = post, categories = categories)
