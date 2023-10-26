from flask import Flask
from flask_mysqldb import MySQL
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL

mysql = MySQL()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY=SECRET_KEY,
            MYSQL_USER=DB_USERNAME,
            MYSQL_PASSWORD=DB_PASSWORD,
            MYSQL_DB=DB_NAME,
            MYSQL_HOST=DB_HOST,
            #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
        )

    mysql.init_app(app)

    from .views import views
    from .student import student as student_blueprint
    from .course import course as course_blueprint
    from .college import college as college_blueprint

    app.register_blueprint(student_blueprint, url_prefix='/')
    app.register_blueprint(course_blueprint, url_prefix='/')
    app.register_blueprint(college_blueprint, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    return app