class ModelInscription:

    @classmethod
    def findByStudentAndCourseId(self, db, idCourse, idStudent):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id FROM inscription WHERE id_user = '{}' AND id_course = '{}'".format(idStudent, idCourse)
            cursor.execute(sql)
            idInscription = cursor.fetchone()
            return idInscription
        except Exception as ex:
            return str(ex)

    @classmethod
    def inscription(self, db, user, courseId):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO inscription (id_user, id_course, role) VALUES(%s, %s, %s);"
            cursor.execute(sql, (user.id, courseId, user.role))
            db.connection.commit()
            return True
        except Exception as ex:
            return str(ex)

    @classmethod
    def findInscriptionByCourseId(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM inscription WHERE id_course = '{}'".format(id)
            cursor.execute(sql)
            inscriptions = cursor.fetchall()
            return inscriptions
        except Exception as ex:
            return str(ex)

    def deregistration(self, db, inscription):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM users_courses WHERE id = %i;"
            cursor.execute(sql, inscription.id)
            db.connection.commit()
            return True
        except Exception as ex:
            return str(ex)