from werkzeug.security import check_password_hash , generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

# clase identica a la bd, es para mapear los objetos de la bd
    def __init__ (self , id, name, last_name, phone, dni, email, password, gender, block , url_image, role="student") -> None:
        self.id = id
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.dni = dni
        self.email = email
        self.password = password
        self.block = block
        self.gender = gender
        self.url_image = url_image
        self.role = role

    @classmethod # no hace falta instanciar clase para usar metodo
    def check_password (self , hashed_password, password):
        return check_password_hash(hashed_password,password)
    
    @classmethod # no hace falta instanciar clase para usar metodo
    def hash_password (self , inputPassword):
        return generate_password_hash(inputPassword)
    