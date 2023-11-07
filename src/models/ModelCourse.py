from models.entities.Course import Course
from models.entities.User import User

class ModelCourse():
    @classmethod
    def findAll(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM course;"
            cursor.execute(sql)
            courses = cursor.fetchall()
            cursor.close()
            return courses
        except Exception as ex:
            return str(ex)
    @classmethod
    def findById(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM course WHERE id = '{}'".format(id)
            cursor.execute(sql)
            courseTupla = cursor.fetchone()
            course = Course(courseTupla[0], courseTupla[1], courseTupla[2], courseTupla[3], courseTupla[4])

            sql = "SELECT * FROM user WHERE id = '{}'".format(course.id_teacher)
            cursor.execute(sql)
            userTupla = cursor.fetchone()
            course.id_teacher = User(userTupla[0], userTupla[1], userTupla[2], userTupla[3], userTupla[4], userTupla[5], userTupla[6], userTupla[8], userTupla[7])
            cursor.close()
            return course
        except Exception as ex:
            return str(ex)
    @classmethod
    def findByName(self, db, name):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM course WHERE name = %s;"
            cursor.execute(sql, name)
            course = cursor.fetchone()
            cursor.close()
            return course
        except Exception as ex:
            return str(ex)
    @classmethod
    def create(self, db, course):
        try:
            print(course.id_teacher)
            cursor = db.connection.cursor()
            sql = "INSERT INTO course (id_teacher, name, duration, description) VALUES(%s, %s, %s, %s);"
            cursor.execute(sql, (course.id_teacher, course.name, course.duration, course.description))
            db.connection.commit()
            cursor.close()
            return True
        except Exception as ex:
            return str(ex)
    @classmethod
    def update(self, db, course, id):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE course SET name = '{}', duration = '{}', description = '{}', id_teacher = '{}' WHERE id = '{}'".format(course.name, course.duration, course.description, course.id_teacher, id)
            cursor.execute(sql)
            db.connection.commit()
            cursor.close()
            return
        except Exception as ex:
            return str(ex)
    @classmethod
    def delete(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM course WHERE id = '{}'".format(id)
            cursor.execute(sql)
            db.connection.commit()
            cursor.close()
            return True
        except Exception as ex:
            return str(ex)