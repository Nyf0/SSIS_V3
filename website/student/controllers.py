from flask import render_template, flash, request, redirect
from . import student
import website.models as models
from website import mysql

@student.route('/students')
def view_studs():
    students = models.Student.all()

    return render_template("students.html", studentdetails=students)

@student.route('/students/add-student', methods=['GET', 'POST'])
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
                student = models.Student(fname=fname, lname=lname, course=course, gender=gender, level=level)
                student.add()
                flash('Student added successfully!', category='success')
                return redirect('/students')
        
    return render_template("add_student.html")

@student.route('/edit-student', methods=['GET', 'POST'])
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
            student = models.Student(id=studID, fname=fname, lname=lname, course=course, gender=gender, level=level)
            student.edit()
            flash('Student edited successfully!', category='success')
        else:
            # The course code doesn't exist in the courses table
            flash('Course does not exist!', category='error')
        cur.close()
    return redirect('/students')

@student.route('/delete-student', methods=['POST'])
def delete_student():
    student_id = request.form.get('student_id')

    if student_id:
        student = models.Student(id=student_id)
        student.delete()
        flash('Student deleted successfully', 'success')
    else:
        flash('Failed to delete the student', 'error')

    return redirect('/students')