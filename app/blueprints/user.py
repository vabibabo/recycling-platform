from flask import Blueprint, render_template, request, redirect, url_for
from .forms import SignupForms
from models import UserModel
from exts import db
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("user", __name__, url_prefix="/")


@bp.route("/")
def index():
    return render_template("homepage.html")
@bp.route("book")
def orderBook():
    return render_template("book.html")

@bp.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        form = SignupForms(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            hash_password = generate_password_hash(password)
            user = UserModel(username=username, password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.signup"))
        else:
            return redirect(url_for("user.signup"))


@bp.route("/login")
def login():
    return render_template("login.html")




