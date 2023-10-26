from flask import Blueprint, render_template, request, flash, redirect
from website import mysql 

create = Blueprint('create', __name__)

@create.route('/add-student', methods=['GET', 'POST'])
def add_student():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        course = request.form.get('student_course')
        gender = request.form.get('gender')
        level = request.form.get('level')

        cur.execute("SELECT code FROM courses WHERE code = %s", (course,))
        cor = cur.fetchone()

        if cor:
            if len(fname) < 1:
                flash('This cannot be empty!', category='error')
            if len(lname) < 1:
                flash('This cannot be empty!', category='error')
            elif len(course) < 1:
                flash('A course must be provided!', category='error')
            else:
                #add student to database
                cur.execute("INSERT INTO students (fname, lname, course, gender, level) VALUES (%s, %s, %s, %s, %s)", (fname, lname, course, gender, level))
                mysql.connection.commit()
                flash('Student added successfully!', category='success')
                cur.close()
                pass
                return redirect('/students')
        else:
            flash('Course does not exist!', category='error')
        
    return render_template("add_student.html")

@create.route('/add-course', methods=['GET', 'POST'])
def add_course():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        code = request.form.get('code')
        name = request.form.get('name')
        college = request.form.get('course_college')

        cur.execute("SELECT code FROM colleges WHERE code = %s", (college,))
        col = cur.fetchone()

        if col:
            if len(code) < 1:
                flash('This cannot be empty!', category='error')
            if len(name) < 1:
                flash('This cannot be empty!', category='error')
            elif len(college) < 1:
                flash('An associated college must exist!', category='error')
            else:
                #add student to database
                cur.execute("INSERT INTO courses (code, name, college) VALUES (%s, %s, %s)", (code, name, college))
                mysql.connection.commit()
                flash('Course added successfully!', category='success')
                cur.close()
                return redirect('/courses')
        else:
            flash('College does not exist!', category='error')

    return render_template("add_course.html")

@create.route('/add-college', methods=['GET', 'POST'])
def add_college():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        code = request.form.get('code')
        name = request.form.get('name')

        if len(code) < 1:
            flash('This cannot be empty!', category='error')
        if len(name) < 1:
            flash('This cannot be empty!', category='error')
        else:
            #add student to database
            cur.execute("INSERT INTO colleges (code, name) VALUES (%s, %s)", (code, name))
            mysql.connection.commit()
            flash('College added successfully!', category='success')
            cur.close()
            return redirect('/colleges')

    return render_template("add_college.html")