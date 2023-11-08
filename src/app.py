from flask import Flask , render_template , request , redirect , url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect  # para que formulario de login tenga codigo token para csrf
from flask_login import LoginManager , login_user, logout_user, login_required, current_user
from flask_mail import Mail
from utils.EmailManager import EmailManager
from dotenv import load_dotenv
from config import config
from config import appConfig
from models.ModelInscription import ModelInscription
from models.ModelCourse import ModelCourse

from models.ModelUser import ModelUser
from models.entities.User import User
from models.entities.Course import Course
# from routers.authRouter import authRouter


load_dotenv()

app = Flask(__name__)
db = MySQL(app)
login_manager_app = LoginManager(app)
#csrf = CSRFProtect(app)  # para que formulario de login tenga codigo token para csrf

mail = Mail(app)

# app.register_blueprint(authRouter)

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
        return render_template('auth/register.html', csrf_token=csrf)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':        
        user = User( 0 , None, None, None, None, request.form['email'], request.form['password'], None )
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
        return render_template('auth/login.html', csrf_token=csrf)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'GET': 
        return render_template('userProfile.html')
    elif request.method == 'POST':
        user = User( 0 ,
            request.form['name'] , 
            request.form['last_name'] , 
            request.form['phone'] , 
            None ,
            request.form['email'] , 
            None ,
            request.form['gender'] ,
            None 
            )
        updatedUser = ModelUser.udpateProfile(db, user)
        if updatedUser:
            flash("Actualizacion correcta!")
            # login_user(updatedUser)
            # return render_template('dashboard.html')
            return redirect(url_for('dashboard'))
        else:
            flash("¡ Error de actualizacion !")
            return render_template('userProfile.html')

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
        courseList = ModelCourse.findAll(db)
        return render_template('dashboard.html', courseList = courseList)
    elif current_user.role == "teacher":        
        courseList = ModelCourse.findAll(db)
        studentList = ModelUser.getAllByRoleForRender(db, "student")
        return render_template('dashboard.html', studentList = studentList, courseList = courseList)
    else:
        courseList = ModelCourse.findAll(db)
        print(courseList)
        studentList = ModelUser.getAllByRoleForRender(db, "student")
        teacherList = ModelUser.getAllByRoleForRender(db, "teacher")
        return render_template('dashboard.html', studentList = studentList, teacherList = teacherList, courseList = courseList)


@app.route("/inscripcion", methods=['GET', 'POST'])
@login_required
def inscription():
    if(request.method == "POST"):
        ModelInscription.inscription(db, current_user, "")
        return
    else:
        courseList = ModelCourse.findAll(db)
        return render_template("inscripcionCurso.html", courseList = courseList, csrf_token = csrf)

@app.route("/add-course", methods=['GET', 'POST'])
@login_required
def addCourse():
    if(request.method == "POST"):
        course = Course(
            None,
            request.form['course_teacher'],
            request.form['course_name'],
            request.form['course_duration'],
            request.form['course_description'])
        ModelCourse.create(db, course)
        return redirect(url_for('dashboard'))
    else:
        teachers = ModelUser.getAllByRoleForRender(db, "teacher")
        return render_template("courseForm.html", csrf_token = csrf, teachers = teachers)

@app.route("/edit-course/<id>", methods=['GET', 'POST'])
@login_required
def editCourse(id):
    if(request.method == "POST" and current_user.role == "admin"):
        course = Course(
            None,
            request.form['course_teacher'],
            request.form['course_name'],
            request.form['course_duration'],
            request.form['course_description'])
        ModelCourse.update(db, course, id)
        return redirect(url_for('dashboard'))
    elif(current_user.role == "admin"):
        course = ModelCourse.findById(db, id)
        teachers = ModelUser.getAllByRoleForRender(db, "teacher")
        return render_template("courseForm.html", csrf_token = csrf, course = course, mode = "edit", teachers = teachers)
    else:
        return render_template("error.html", message="Usted no posee los privilegios para acceder a esta URL.")

@app.route("/delete-course/<id>", methods=['GET'])
@login_required
def deleteCourse(id):
    if(current_user.role == "admin"):
        course = ModelCourse.findById(db, id)
        return render_template("delete.html", csrf_token = csrf, course = course)
    else:
        return render_template("error.html", message="Usted no posee los privilegios para acceder a esta URL.")

@app.route("/delete-course", methods=['POST'])
@login_required
def deleteCoursePost():
    idCourse = request.form['id_course']
    if (not idCourse.isnumeric()):
        return render_template("error.html", message="Url no valida.")
    elif (current_user.role == "admin"):
        ModelCourse.delete(db, idCourse)
        return redirect(url_for('dashboard'))
    else:
        return render_template("error.html", message="Usted no posee los privilegios para acceder a esta URL.")

@app.route("/edit-user/<id>", methods=['GET'])
def editUser(id):
    return

def status_401(error):
     return redirect(url_for('login'))

def status_404(error):
     return "<h1> Pagina no encontrada! <h1/>",404
# ------------------ MANEJO DE ERRORES ------------------

if __name__ == '__main__':
    app.config.from_object(config['development'])
    appConfig.init(app)
    csrf = CSRFProtect()  # para que formulario de login tenga codigo token para csrf
    # csrf.init_app(app) # para que formulario de login tenga codigo token para csrf
    mail.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()