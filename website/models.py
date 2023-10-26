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

        sql = f"INSERT INTO students (fname, lname, course, gender, level) VALUES ('{self.fname}','{self.lname}','{self.course}','{self.gender}','{self.level}')"
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from students"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

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
            cursor.close()
            return True
        except:
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

