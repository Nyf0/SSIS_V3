from flask import Blueprint, render_template, request
from website import mysql

views = Blueprint('views', __name__)

@views.route('/')
def home():
    cur = mysql.connection.cursor()
    # Select data from the students, courses, and colleges tables
    sql = f"SELECT * FROM students ORDER BY student_id DESC LIMIT 5"
    cur.execute(sql)
    students = cur.fetchall()

    cur.execute("SELECT * FROM courses ORDER BY code DESC LIMIT 5")
    courses = cur.fetchall()

    cur.execute("SELECT * FROM colleges ORDER BY code DESC LIMIT 5")
    colleges = cur.fetchall()

    return render_template("home.html", students=students, courses=courses, colleges=colleges)

@views.route('/search', methods=['GET', 'POST'])
def search():
    search_term = request.form['search_term']
    
    cur = mysql.connection.cursor()

    # Construct and execute the SQL query
    studquery = f"SELECT * FROM students WHERE student_id LIKE '{search_term}' OR fname LIKE '%{search_term}%' OR lname LIKE '%{search_term}%' OR course LIKE '{search_term}' OR gender LIKE '{search_term}' OR level LIKE '{search_term}'"
    cur.execute(studquery)
    students = cur.fetchall()

    corquery = f"SELECT * FROM courses WHERE code LIKE '{search_term}' OR name LIKE '%{search_term}%' OR college LIKE '%{search_term}%'"
    cur.execute(corquery)
    courses = cur.fetchall()

    colquery = f"SELECT * FROM colleges WHERE code LIKE '{search_term}' OR name LIKE '%{search_term}%'"
    cur.execute(colquery)
    colleges = cur.fetchall()

    # Close the database connection
    cur.close()

    return render_template('search.html', students=students, courses=courses, colleges=colleges)

