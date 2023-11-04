class ModelInscription:
    def inscription(self, db, user, course):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO users_courses VALUES(null, %i, %i, %s);"
            cursor.execute(sql, user.id, course.id, user.role)
            db.connection.commit()
            return True
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