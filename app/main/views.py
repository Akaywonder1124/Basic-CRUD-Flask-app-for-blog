from flask import Blueprint, render_template, request
from ..model import Post
from sqlalchemy import desc
from app import db
main = Blueprint("main", __name__)


@main.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    post = db.session.query(Post).order_by(desc(Post.id)).paginate(page=page, per_page=6)
    return render_template("homepage.html", post = post)
        

@main.route("/about")
def about():
    return render_template("about.html")

@main.app_context_processor
def context_processor():
    posts = db.session.query(Post).order_by(Post.id.desc()).group_by(Post.categories).limit(9)
    #posts = db.session.query(Post).filter(Post.id == db.session.query(max(Post.id)))
    #posts = Post.query.filter_by(id = 1).first()

    page = request.args.get("page", 1, type=int)
    post = db.session.query(Post).order_by(desc(Post.id)).limit(6)
    post1 = db.session.query(Post).order_by(desc(Post.categories)).paginate(page=page, per_page=4)
    return dict(posts = posts, header_post=post, carousel_post = post1)