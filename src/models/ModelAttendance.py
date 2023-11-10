class ModelAttendance:
    @classmethod
    def takeAttendance(self, db, attendance):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO attendance (id_inscription, date, present) VALUES (%s, %s, %s);"
            cursor.execute(sql, (attendance.idInscription, attendance.date, attendance.present))
            db.connection.commit()
            cursor.close()
            return True
        except Exception as ex:
            return str(ex)