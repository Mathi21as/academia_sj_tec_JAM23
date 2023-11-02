from flask import Flask , render_template , request , redirect , url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect  # para que formulario de login tenga codigo token para csrf
from flask_login import LoginManager , login_user, logout_user, login_required, current_user
from flask_mail import Mail
from utils.EmailManager import EmailManager
from dotenv import load_dotenv
from config import config

from models.ModelUser import ModelUser
from models.entities.User import User
# from routers.authRouter import authRouter


load_dotenv()

app = Flask(__name__)
db = MySQL(app) 
login_manager_app = LoginManager(app)
csrf = CSRFProtect()  # para que formulario de login tenga codigo token para csrf

mail = Mail()

# app.register_blueprint(authRouter)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db , id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == "student":
        return render_template('dashboard.html')
    elif current_user.role == "teacher":
        studentList = ModelUser.getAllByRoleForRender(db, "student")
        return render_template('dashboard.html', studentList = studentList)
    elif current_user.role == "admin":
        studentList = ModelUser.getAllByRoleForRender(db, "student")
        teacherList = ModelUser.getAllByRoleForRender(db, "teacher")
        return render_template('dashboard.html', studentList = studentList, teacherList = teacherList)


# ------------------ CURSOS ------------------
# ------------------ CURSOS ------------------
@app.route('/course', methods=['GET', 'POST'])
@login_required
def course():
    if current_user.role == "student":
        return render_template('dashboard.html')
    elif current_user.role == "teacher" or current_user.role == "admin":
        if request.method == 'GET' :
            return render_template('courseAddForm.html')
        elif request.method == 'POST':
            print("AGREGANDO CURSO! ------------------ CURSOS ------------------")
            print("AGREGANDO CURSO! ------------------ CURSOS ------------------")
            print("AGREGANDO CURSO! ------------------ CURSOS ------------------")
            print("AGREGANDO CURSO! ------------------ CURSOS ------------------")
            print("AGREGANDO CURSO! ------------------ CURSOS ------------------")
        elif request.method == 'PUT':
            print("EDITANDO CURSO! ------------------ CURSOS ------------------")
            print("EDITANDO CURSO! ------------------ CURSOS ------------------")
            print("EDITANDO CURSO! ------------------ CURSOS ------------------")
            print("EDITANDO CURSO! ------------------ CURSOS ------------------")
            






# ------------------ CURSOS ------------------


# ------------------ SESIONES ------------------
# ------------------ SESIONES ------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':      
        if request.form['password'] == request.form['password-confirm']:     
            user = User( 0 ,
                        request.form['name'] , 
                        request.form['last_name'] , 
                        request.form['phone'] , 
                        request.form['dni'] ,
                        request.form['email'] , 
                        request.form['password'], 
                        request.form['gender'] 
                        )
            registerUser = ModelUser.register(db, user)
            if registerUser:                 
                loguedUser = ModelUser.login(db, user)
                login_user(loguedUser)                
                EmailManager.sendEmail(user.email)
                return redirect(url_for('dashboard'))
            else:                
                flash("Email ya existe, intenta logueandote")
                return render_template('auth/login.html')
        else:            
            flash("Passwords no coinciden!")
            return render_template('auth/register.html')
    else:
        return render_template('auth/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':        
        user = User( 0 , None, None, None, None, request.form['email'], request.form['password'] , None)
        loguedUser = ModelUser.login(db, user)

        if loguedUser != None:
            if loguedUser.password:
                login_user(loguedUser)
                return redirect(url_for('dashboard'))
            else:
                flash("Credenciales erroneas")
                return render_template('auth/login.html')
        else:
            flash("Credenciales erroneas")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
# ------------------ SESIONES ------------------


# ------------------ MANEJO DE ERRORES ------------------
# ------------------ MANEJO DE ERRORES ------------------
def status_401(error):
     return redirect(url_for('login'))

def status_404(error):
     return "<h1> Pagina no encontrada! <h1/>",404
# ------------------ MANEJO DE ERRORES ------------------

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app) # para que formulario de login tenga codigo token para csrf
    mail.init_app(app)
    app.register_error_handler(401 , status_401)
    app.register_error_handler(404 , status_404)
    app.run()