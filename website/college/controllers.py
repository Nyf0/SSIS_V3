from flask import render_template, flash, request, redirect
from . import college
import website.models as models

@college.route('/colleges')
def cols():
    colleges = models.College.all()

    return render_template("colleges.html", collegedetails=colleges)
    
@college.route('/add-college', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        code = request.form.get('code')
        name = request.form.get('name')

        if len(code) < 1:
            flash('This cannot be empty!', category='error')
        if len(name) < 1:
            flash('This cannot be empty!', category='error')
        else:
            #add college to database
            college = models.College(code=code, name=name)
            college.add()
            flash('College added successfully!', category='success')
            return redirect('/colleges')

    return render_template("add_college.html")

@college.route('/edit-college', methods=['GET', 'POST'])
def edit_college():
    if request.method == 'POST':
        code = request.form.get('code')
        name = request.form.get('name')
        new = request.form.get('newcode')

        if code == new:
            college = models.College(code=code, name=name)
            college.edit()
            flash('College editted successfully!', category='success')
        else:
            check = models.College.check_code(new)

            if check:
                flash('This College code is already in use! Try another one.', category='error')
            else:
                college = models.College(code=code, name=name)
                college.edit()
                college.editcode(new)
                flash('College editted successfully!', category='success')
    
    return redirect('/colleges')

@college.route('/delete-college', methods=['POST'])
def delete_college():
    code = request.form.get('code')

    if code:
        college = models.College(code=code)
        college.delete()
        flash('College deleted successfully', 'success')
    else:
        flash('Failed to delete the college', 'error')

    return redirect('/colleges')
