from flask import Blueprint, request, flash, redirect
from website import mysql

change = Blueprint('change', __name__)

@change.route('/edit-student', methods=['GET', 'POST'])
def edit_student():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        studID = request.form.get('ID')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        course = request.form.get('course')
        gender = request.form.get('gender')
        level = request.form.get('level')

        # Get the course code from the form
        course_code = request.form.get('course')

        # Check if the course code exists in the courses table
        cur.execute("SELECT code FROM courses WHERE code = %s", (course_code,))
        existing_course = cur.fetchone()

        if existing_course:
            # The course code exists, so you can proceed with the UPDATE query
            cur.execute("UPDATE students SET fname = %s, lname = %s, course = %s, gender = %s, level = %s WHERE student_id = %s", (fname, lname, course, gender, level, studID))
            mysql.connection.commit()
            flash('Student edited successfully!', category='success')
        else:
            # The course code doesn't exist in the courses table
            flash('Course does not exist!', category='error')
        cur.close()
    return redirect('/students')

@change.route('/edit-course', methods=['GET', 'POST'])
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
            cur.execute("UPDATE courses SET name = %s, college = %s WHERE code = %s", (name, college, code))
            mysql.connection.commit()
            flash('Course editted successfully!', category='success')
        else:
            # The college code doesn't exist in the colleges table
            flash('College does not exist!', category='error')
        cur.close()
    
    return redirect('/courses')

@change.route('/edit-college', methods=['GET', 'POST'])
def edit_college():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        code = request.form.get('code')
        name = request.form.get('name')

        cur.execute("UPDATE colleges SET name = %s WHERE code = %s", (name, code))
        mysql.connection.commit()
        flash('College editted successfully!', category='success')
        cur.close()
    
    return redirect('/colleges')