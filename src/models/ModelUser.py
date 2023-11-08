from models.entities.User import User
from flask_mysqldb import MySQL


class ModelUser():

    @classmethod
    def register(self , db, user):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO user (`name`, `last_name`, `phone`, `dni`, `email`, `password`, `role`, `gender`)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            if user.email == "admin@admin.com" :
                user.role = "admin"
            cursor.execute(sql, (                
                user.name, 
                user.last_name, 
                user.phone, 
                user.dni, 
                user.email, 
                User.hash_password(user.password), 
                user.role,
                user.gender))
            db.connection.commit()
            cursor.close()

            return True
        except Exception as ex:
            if ex.args[0] == 1062:
                return False
            return str(ex)

    @classmethod
    def udpateProfile( self , db, user) :
        try:            
            print(user.name, user.last_name, user.phone, user.gender, user.email)
            cursor = db.connection.cursor()
            sql = "UPDATE user SET `name` = '{}', `last_name` = '{}', `phone` = '{}',  `gender` = '{}' WHERE email = '{}'".format(user.name, user.last_name, user.phone, user.gender, user.email)
            cursor.execute(sql)
            db.connection.commit()
            cursor.close()
            return True
        except Exception as ex:
            print(str(ex))
            print(str(ex))
            print(str(ex))
            print(str(ex))
            return False


    @classmethod
    def login(self , db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, name, last_name, phone, dni, email, password, gender, role FROM user 
                        WHERE email = '{}'""".format(user.email)
            cursor.execute(sql)
            row = cursor.fetchone()
            cursor.close()
            if row != None:
                validPassword = User.check_password(row[6] , user.password)
                return User(row[0], row[1], row[2], row[3], row[4], row[5] , validPassword, row[7], row[8])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self , db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, name, last_name, phone, dni, email,gender, role  FROM user 
                        WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            cursor.close()
            if row != None:
                return User(row[0], row[1], row[2], row[3], row[4], row[5] , None, row[6], row[7])
            else:
                return None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update(self, db, user):
        return

    @classmethod
    def getAllByRoleForRender(self , db, role):
        try:
            userList = []
            cursor = db.connection.cursor()
            sql = """SELECT id, name, last_name, phone, dni, email, gender FROM user 
                        WHERE role = '{}'""".format(role)
            cursor.execute(sql)
            rows = cursor.fetchall()
            cursor.close()
            for row in rows:
                userData =[row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
                userList.append(userData)
            return userList
        
        except Exception as ex:
            raise Exception(ex)       
