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
            sql = """UPDATE user SET `name` = '{}', `last_name` = '{}', `phone` = '{}',  `gender` = '{}' 
                        WHERE email = '{}'""".format(user.name, user.last_name, user.phone, user.gender, user.email)
            cursor.execute(sql)
            db.connection.commit()
            cursor.close()
            return True
        except Exception as ex:
            print(str(ex))
            return False

    @classmethod
    def login(self , db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, name, last_name, phone, dni, email, password, gender, block, role   FROM user 
                        WHERE email = '{}'""".format(user.email)
            cursor.execute(sql)
            row = cursor.fetchone()
            cursor.close()
            if row != None:
                validPassword = User.check_password(row[6] , user.password)
                return User(row[0], row[1], row[2], row[3], row[4], row[5] , validPassword, row[7], row[8], row[9])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self , db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, name, last_name, phone, dni, email,gender, block, role  FROM user 
                        WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            cursor.close()
            if row != None:
                return User(row[0], row[1], row[2], row[3], row[4], row[5] , None, row[6], row[7], row[8])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    
    @classmethod
    def modifyBlockUser( self , db, id) :
        try:            
            cursor = db.connection.cursor()
            sql = """SELECT block  FROM user 
                        WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            blockState = cursor.fetchone()[0]
            state = 0 if blockState == 1 else 1
            sql2 = "UPDATE user SET `block` = '{}' WHERE id = '{}'".format(state,id)
            cursor.execute(sql2)
            db.connection.commit()
            cursor.close()
            return True
        except Exception as ex:
            print(str(ex))
            return False
        
    @classmethod
    def getAllInscriptedStudentsByIdCourse(self, db, idCourse):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT u.id, u.name, u.last_name, u.phone, u.dni, u.email, u.gender, u.block FROM inscription
                        JOIN user u ON id_user = u.id
                        WHERE id_course ={};""".format(idCourse)
            cursor.execute(sql)
            courses = cursor.fetchall()
            return courses
        except Exception as ex:
            return str(ex)

#
#    @classmethod
#    def update(self, db, user):
#        try:
#            cursor = db.connection.cursor()
#            sql = """UPDATE user SET name = '{}', last_name = '{}',phone = '{}', dni = '{}', email = '{}',
#                password = '{}', role = '{}'  WHERE email = '{}'""".format(user.name, user.last_name, user.phone, user.dni,
#                                                       user.email, user.password, user.role, user.email)
#            cursor.execute(sql)
#            db.connection.commit()
#            cursor.close()
#            return True
#
#        except Exception as ex:
#            raise Exception(ex)
    @classmethod
    def updateByAdmin(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE user SET name = '{}', last_name = '{}', phone = '{}', role = '{}'  WHERE id = '{}'"\
                .format(user.name, user.last_name, user.phone, user.role, user.id)
            cursor.execute(sql)
            db.connection.commit()
            cursor.close()
            return True
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def getAllByRoleForRender(self , db, role):
        try:
            userList = []
            cursor = db.connection.cursor()
            sql = """SELECT id, name, last_name, phone, dni, email, block, gender  FROM user 
                        WHERE role = '{}'""".format(role)
            cursor.execute(sql)
            rows = cursor.fetchall()
            cursor.close()
            for row in rows:
                userData =[row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
                userList.append(userData)
            return userList
        
        except Exception as ex:
            raise Exception(ex)       
