from flask import render_template, flash, request, redirect
from . import course
import website.models as models
from website import mysql

@course.route('/courses')
def curs():
    courses = models.Course.all()

    return render_template("courses.html", coursedetails=courses)

@course.route('/add-course', methods=['GET', 'POST'])
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
                course = models.Course(code=code, name=name, college=college)
                course.add()
                flash('Course added successfully!', category='success')
                cur.close()
                return redirect('/courses')
        else:
            flash('College does not exist!', category='error')

    return render_template("add_course.html")

@course.route('/edit-course', methods=['GET', 'POST'])
def edit_course():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        code = request.form.get('code')
        name = request.form.get('name')
        college = request.form.get('college')

        # Get the college code from the form
        college_code = request.form.get('college')

        # Check if the college exists in the colleges table
        cur.execute("SELECT code FROM colleges WHERE code = %s", (college_code,))
        existing_college = cur.fetchone()

        if existing_college:
            # The college exists, so you can proceed with the UPDATE query
            course = models.Course(code=code, name=name, college=college)
            course.edit()
            flash('Course editted successfully!', category='success')
        else:
            # The college code doesn't exist in the colleges table
            flash('College does not exist!', category='error')
        cur.close()
    
    return redirect('/courses')

@course.route('/delete-course', methods=['POST'])
def delete_course():
    code = request.form.get('course_code')

    if code:
        course = models.Course(code=code)
        course.delete()
        flash('Course deleted successfully', 'success')
    else:
        flash('Failed to delete the Course', 'error')

    return redirect('/courses')