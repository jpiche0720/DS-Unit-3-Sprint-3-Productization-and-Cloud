from flask import Flask

from web_app.db_models import db, migrate
from web_app.routes.home_routes import home_routes


DATABASE_URI = "sqlite:////DS-Unit-3-Sprint-3-Productization-and-Cloud/web_app/web_app_data.db"

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)




