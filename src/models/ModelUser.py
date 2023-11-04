from models.entities.User import User
from flask_mysqldb import MySQL


class ModelUser():

    @classmethod
    def register(self , db, user):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO user (`name`, `last_name`, `phone`, `dni`, `email`, `password`, `role`)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            if user.email == "admin@admin.com" :
                user.role = "admin"
            cursor.execute(sql, (                
                user.name, 
                user.last_name, 
                user.phone, 
                user.dni, 
                user.email, 
                User.hash_password(user.password), 
                user.role))
            db.connection.commit()            
            return True
        except Exception as ex:
            if ex.args[0] == 1062:
                return False
            return str(ex)


    @classmethod
    def login(self , db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, name, last_name, phone, dni, email, password, role FROM user 
                        WHERE email = '{}'""".format(user.email)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                validPassword = User.check_password(row[6] , user.password)
                return User(row[0], row[1], row[2], row[3], row[4], row[5] , validPassword, row[7])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self , db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, name, last_name, phone, dni, email, role FROM user 
                        WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()

            if row != None:
                return User(row[0], row[1], row[2], row[3], row[4], row[5] , None, row[6])
            else:
                return None

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def getAllByRoleForRender(self , db, role):
        try:
            userList = []
            cursor = db.connection.cursor()
            sql = """SELECT id, name, last_name, phone, dni, email FROM user 
                        WHERE role = '{}'""".format(role)
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            for row in rows:
                userData =[row[0], row[1], row[2], row[3], row[4], row[5]]
                userList.append(userData)
            return userList
        
        except Exception as ex:
            raise Exception(ex)       
