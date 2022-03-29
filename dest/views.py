from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    background_image = "haus.jpeg"
    return render_template("home.html", background_image=background_image)

@views.route("/produkte")
def produkte():
    background_image = "derGin.jpeg"
    return render_template("produkte.html", background_image=background_image)

@views.route("/philosophie")
def philosophie():
    background_image = "pineapple.jpg"
    return render_template("philosophie.html", background_image=background_image)

@views.route("/verkostungen")
def verkostungen():
    background_image = "küche.jpeg"
    return render_template("verkostungen.html", background_image=background_image)