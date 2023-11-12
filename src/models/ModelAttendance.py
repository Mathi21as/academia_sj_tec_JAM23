import datetime as dt

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

    @classmethod
    def findCountAttendanceOfAStudent(self, db, idInscription):
        try:
            today = dt.date()
            date = str(today).replace(today.month, today.month+1)
            cursor = db.connection.cursor()
            sql = "SELECT COUNT(*) FROM attendance WHERE id_inscription = '{}' AND date BETWEEN '{}' AND '{}'"\
                .format(idInscription, today, date)
            cursor.execute(sql)
            attendance = cursor.fetchall()
            print(attendance)
            return attendance
        except Exception as ex:
            return str(ex)