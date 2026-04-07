from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/about")
def about():
    return "About page"