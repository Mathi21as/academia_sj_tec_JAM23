class ModelAttendance:
    @classmethod
    def takeAttendance(self, db, attendance):
        try:            
            cursor = db.connection.cursor()
            sql = "INSERT INTO attendance (id_inscription, date, present) VALUES (%s, %s, %s);"
            cursor.execute(sql, (attendance.idInscription[0], attendance.date, attendance.present))
            db.connection.commit()
            cursor.close()
            return True
        except Exception as ex:
            return str(ex)

    @classmethod
    def findCountAttendanceOfAStudent(self, db, idInscription):
        try:
            #date =
            cursor = db.connection.cursor()
            sql = "SELECT COUNT(*) FROM attendance WHERE id_inscription = %s AND date > "
            cursor.execute(sql, idInscription)
            attendance = cursor.fetchall()
            return attendance
        except Exception as ex:
            return str(ex)