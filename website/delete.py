from flask import Blueprint, render_template, request, flash, redirect
from website import mysql 

delete = Blueprint('delete', __name__)

@delete.route('/delete-student', methods=['POST'])
def delete_student():
    student_id = request.form.get('student_id')

    if student_id:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        mysql.connection.commit()
        flash('Student deleted successfully', 'success')
    else:
        flash('Failed to delete the student', 'error')

    return redirect('/students')

@delete.route('/delete-course', methods=['POST'])
def delete_course():
    code = request.form.get('course_code')

    if code:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM courses WHERE code = %s", (code,))
        mysql.connection.commit()
        flash('Course deleted successfully', 'success')
    else:
        flash('Failed to delete the Course', 'error')

    return redirect('/courses')

@delete.route('/delete-college', methods=['POST'])
def delete_college():
    code = request.form.get('code')

    if code:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM colleges WHERE code = %s", (code,))
        mysql.connection.commit()
        flash('College deleted successfully', 'success')
    else:
        flash('Failed to delete the college', 'error')

    return redirect('/colleges')
