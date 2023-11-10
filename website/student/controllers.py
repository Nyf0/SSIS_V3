from flask import render_template, flash, request, redirect
from . import student
import website.models as models
import re

@student.route('/students')
def view_studs():
    students = models.Student.all()
    courses = models.Course.all()

    return render_template("students.html", studentdetails=students, courses = courses)

@student.route('/students/add-student', methods=['GET', 'POST'])
def add_student():
    courses = models.Course.all()

    if request.method == 'POST':
        id = request.form.get('id')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        course = request.form.get('student_course')
        gender = request.form.get('gender')
        level = request.form.get('level')

        cor = models.Student.check_course(course)
        exists = models.Student.check_id(id)

        if exists:
            flash('This ID already exists!', category='error')
        else:
            if cor:
                if len(fname) < 1:
                    flash('This cannot be empty!', category='error')
                if len(lname) < 1:
                    flash('This cannot be empty!', category='error')
                elif len(course) < 1:
                    flash('A course must be provided!', category='error')
                else:
                    #add student to database
                    student = models.Student(id=id, fname=fname, lname=lname, course=course, gender=gender, level=level)
                    student.add()
                    flash('Student added successfully!', category='success')
                    return redirect('/students')
            else:
                flash('Course does not exist!', category='error')
        
    return render_template("add_student.html", courses = courses)

@student.route('/edit-student', methods=['GET', 'POST'])
def edit_student():
    if request.method == 'POST':
        studID = request.form.get('id')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        course = request.form.get('course')
        gender = request.form.get('gender')
        level = request.form.get('level')
        newID = request.form.get('newID')

        if not studID or not fname or not lname or not gender or not course or not level:
            flash('Please fill out all fields!', category='error')
            return redirect('/students')

        # Check if the new ID follows the right format
        if not re.match(r'^\d{4}-\d{4}$', newID):
            flash('New ID should follow the format YYYY-NNNN', category='error')
            return redirect('/students')
        
        # Check if the gender is valid
        if gender not in ['Male', 'Female']:
            flash('Gender should be "Male" or "Female"', category='error')
            return redirect('/students')
        
        # Check if the course code exists in the courses table
        existing_course = models.Student.check_course(course)

        # Check if the ID is updated
        if newID == studID:
            if existing_course:
                # The course code exists, so you can proceed with the UPDATE query
                student = models.Student(id=studID, fname=fname, lname=lname, course=course, gender=gender, level=level)
                student.edit()
                
                flash('Student edited successfully!', category='success')
            else:
                    # The course code doesn't exist in the courses table
                    flash('Course does not exist!', category='error')
        else:
            # Checks if the new id input is already used
            checkID = models.Student.check_id(newID)
            if checkID:
                flash('ID already exists! Try another one!', category='error')
            else:
                if existing_course:
                    # The course code exists, so you can proceed with the UPDATE query
                    student = models.Student(id=studID, fname=fname, lname=lname, course=course, gender=gender, level=level)
                    # Normal edit first
                    student.edit()
                    # Then change the ID
                    student.editID(newID)
                    
                    flash('Student edited successfully!', category='success')
                else:
                    # The course code doesn't exist in the courses table
                    flash('Course does not exist!', category='error')
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