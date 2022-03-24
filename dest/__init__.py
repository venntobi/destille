from flask import Flask, render_template, url_for, json

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "1234"
    
    from .views import views
    
    app.register_blueprint(views, url_prefix="/")
    
    return app

