class ModelCourse():
    @classmethod
    def findAll(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM course;"
            cursor.execute(sql)
            courses = cursor.fetchall()
            return courses
        except Exception as ex:
            return str(ex)
    @classmethod
    def findById(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM course WHERE id = %i;"
            cursor.execute(sql, id)
            course = cursor.fetchone()
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
            return course
        except Exception as ex:
            return str(ex)
    @classmethod
    def create(self, db, course):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO course VALUES(null, %s, %s, %i);"
            cursor.execute(sql, course.name, course.description, course.idTeacher)
            db.connection.commit()
            db.connection.close()
            return True
        except Exception as ex:
            return str(ex)
    @classmethod
    def update(self, db, course, id):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE course VALUES(null, );"
            cursor.execute(sql, ) #TODO: buscar la manera de actualizar solo los campos solicitados
            db.connection.commit()
            return
        except Exception as ex:
            return str(ex)
    @classmethod
    def delete(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM course WHERE id = %i;"
            cursor.execute(sql, id)
            db.connection.commit()
            return True
        except Exception as ex:
            return str(ex)