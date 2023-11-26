
from flask import Flask, render_template

from flask_mysqldb import MySQL

app=Flask(__name__)

@app.route('/')
def index():
    grupo="IEVN-1002"
    lista=["IEVN 1001", "IEVN 1002", "IEVN 1003"]
    return render_template('index.html',grupo=grupo,lista=lista)

@app.route('/hola')
def hola():
    
    return "Saldos compa"

@app.route('/user/<string:nombre>')
def user(nombre):
    return 'Saldos {}'.format(nombre)

@app.route('/numero/<int:n1>')
def numero(n1):
    return 'El número es {}'.format(n1)

@app.route('/user/<int:id>/<string:nom>')
def user1(id,nom):
    return 'ID: {} Nombre: {}'.format(id,nom)

@app.route('/suma/<float:sn1>/<float:sn2>')
def suma(sn1,sn2):
    return 'La suma es: {}'.format(sn1+sn2)

@app.route('/default')
@app.route('/default/<string:dd>')
def defult(dd='texto'):
    return '<h1>El sitio muestra: </h1>'.format(dd)

@app.route('/alunos')
def alumnos():
    return render_template('alumnos.html')

if __name__ == "__main__":
    app.run(debug=True)