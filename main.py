from flask import Flask, request, render_template, Response
from flask_wtf.csrf import CSRFProtect
from flask import flash
from flask import g
import forms
from config import DevelopmentConfig
from models import db
from models import Alumnos

app=Flask(__name__) 
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.errorhandler(400)
def page_not_found(e):
    return render_template('404.html'),404

@app.route("/index", methods=["GET", "POST"])
def index():
    alum_form=forms.UserForm2(request.form)
    if request.method=='POST' and alum_form.validate():
        alum=Alumnos(nombre=alum_form.nombre.data,
                     apaterno=alum_form.apaterno.data,
                     email=alum_form.email.data)
        """ insert into alumnos values() """
        db.session.add(alum)
        db.session.commit()
    return render_template("index.html", form=alum_form)

@app.route("/ABC_Completo", methods=["GET", "POST"])
def ABDCompleto():
    create_form=forms.UserForm2(request.form)

    alumno=Alumnos.query.all()
    return render_template("ABC_Completo.html", alumno=alumno)


@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    nom=''
    alum_form=forms.UserForm(request.form)
    if request.method=='POST' and alum_form.validate():
        nom=alum_form.nombre.data
        apaterno=alum_form.apaterno.data
        amaterno=alum_form.amaterno.data
        edad=alum_form.edad.data
        email=alum_form.email.data
        mensaje='Bienvenido: {}'.format(nom)
        flash(mensaje)
        print('Apaterno: {}'.format(apaterno))
        print('Amaterno: {}'.format(amaterno))
        print('Edad: {}'.format(edad))
        print('Correo: {}'.format(email))
        return render_template("alumnos.html", form=alum_form, nom=nom)
    else:
        return render_template("alumnos.html", form=alum_form)
if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()