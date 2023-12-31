from website import mysql

class Student(object):
    def __init__(self, id=None, fname=None, lname=None, course=None, gender=None, level=None):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.course = course
        self.gender = gender
        self.level = level

    def add(self):
        cur = mysql.connection.cursor()

        sql = f"INSERT INTO students (student_id, fname, lname, course, gender, level) VALUES ('{self.id}','{self.fname}','{self.lname}','{self.course}','{self.gender}','{self.level}')"
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def show(self):
        cur = mysql.connection.cursor()
        sql = f"SELECT * FROM students ORDER BY student_id DESC LIMIT 5"
        cur.execute(sql)
        students = cur.fetchall()
        return students
    
    def search(key):
        cur = mysql.connection.cursor()
        studquery = f"SELECT students.student_id, students.fname, students.lname, students.course, students.gender, students.level, colleges.code, colleges.name FROM students INNER JOIN courses ON students.course = courses.code INNER JOIN colleges ON courses.college = colleges.code WHERE students.student_id LIKE '{key}' OR students.fname LIKE '%{key}%' OR students.lname LIKE '%{key}%' OR students.course LIKE '{key}' OR students.gender LIKE '{key}' OR students.level LIKE '{key}'"
        cur.execute(studquery)
        results = cur.fetchall()
        return results

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from students"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def check_course(course):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code FROM courses WHERE code = %s", (course,))
        cor = cur.fetchone()
        return cor
    
    def check_id(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT student_id FROM students WHERE student_id = %s", (id,))
        ids = cur.fetchone()

        return ids

    def delete(self):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from students where student_id= '{self.id}'"
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.close()
            return True
        except:
            return False
        
    def edit(self):
        try:
            cursor = mysql.connection.cursor()
            sql = f"UPDATE students SET fname = '{self.fname}', lname = '{self.lname}', course = '{self.course}', gender = '{self.gender}', level = '{self.level}' WHERE student_id = '{self.id}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def editID(self, newID):
        try:
            cursor = mysql.connection.cursor()
            sql = f"UPDATE students SET student_id = '{newID}' WHERE student_id = '{self.id}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
class Course(object):
    def __init__(self, code=None, name=None, college=None):
        self.code = code
        self.name = name
        self.college = college

    def add(self):
        cur = mysql.connection.cursor()

        sql = f"INSERT INTO courses (code, name, college) VALUES ('{self.code}','{self.name}','{self.college}')"
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * FROM courses"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def show(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM courses ORDER BY code DESC LIMIT 5")
        courses = cur.fetchall()
        return courses
    
    def search(key):
        cur = mysql.connection.cursor()
        corquery = f"SELECT * FROM courses WHERE code LIKE '{key}' OR name LIKE '%{key}%' OR college LIKE '%{key}%'"
        cur.execute(corquery)
        results = cur.fetchall()
        return results
    
    def check_college(college):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code FROM colleges WHERE code = %s", (college,))
        col = cur.fetchone()
        return col
    
    def get():
        cur = mysql.connection.cursor()
        cur.execute("SELECT students.student_id, students.fname, students.lname, students.course, students.gender, students.level, colleges.code, colleges.name FROM students INNER JOIN courses ON students.course = courses.code INNER JOIN colleges ON courses.college = colleges.code")
        col = cur.fetchall()
        return col

    def check_code(code):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code FROM courses WHERE code = %s", (code,))
        code = cur.fetchone()

        return code

    def delete(self):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from courses where code = '{self.code}'"
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.close()
            return True
        except:
            return False
        
    def edit(self):
        try:
            cursor = mysql.connection.cursor()
            sql = f"UPDATE courses SET name = '{self.name}', college = '{self.college}' WHERE code = '{self.code}'"
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.close()
            return True
        except:
            return False
        
    def editcode(self, newcode):
        try:
            cursor = mysql.connection.cursor()
            sql = f"UPDATE courses SET code = '{newcode}' WHERE code = '{self.code}'"
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.close()
            return True
        except:
            return False

class College(object):
    def __init__(self, code=None, name=None):
        self.code = code
        self.name = name

    def add(self):
        cur = mysql.connection.cursor()

        sql = f"INSERT INTO colleges (code, name) VALUES ('{self.code}','{self.name}')"
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * FROM colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def show(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM colleges ORDER BY code DESC LIMIT 5")
        colleges = cur.fetchall()
        return colleges
    
    def search(key):
        cur = mysql.connection.cursor()
        colquery = f"SELECT * FROM colleges WHERE code LIKE '{key}' OR name LIKE '%{key}%'"
        cur.execute(colquery)
        results = cur.fetchall()
        return results
    

    def delete(self):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from colleges where code = '{self.code}'"
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.close()
            return True
        except:
            return False
        
    def check_code(code):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code FROM colleges WHERE code = %s", (code,))
        code = cur.fetchone()

        return code
        
    def edit(self):
        try:
            cursor = mysql.connection.cursor()
            sql = f"UPDATE colleges SET name = '{self.name}' WHERE code = '{self.code}'"
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.close()
            return True
        except:
            return False
        
    def editcode(self, new):
        try:
            cursor = mysql.connection.cursor()
            sql = f"UPDATE colleges SET code = '{new}' WHERE code = '{self.code}'"
            cursor.execute(sql)
            mysql.connection.commit()
            cursor.close()
            return True
        except:
            return False

