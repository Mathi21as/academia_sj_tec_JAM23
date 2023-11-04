class ModelAttendance:
    def takeAttendance(self, db, attendance):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO attendance VALUES(%i, %i, %s, %i);"
            cursor.execute(sql, attendance.id, attendance.idInscription, attendance.date, attendance.present)
            db.connection.commit()
            return True
        except Exception as ex:
            return str(ex)