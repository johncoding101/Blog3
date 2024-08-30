# -*- coding: utf-8 -*-
'''
Created on Monday Aug 19 20:16:10 2024
Udemy -100 Days of code (Angela Yu)
video -468 Requirement 2 - Be Able to POST a New Blog Post
Author: JohnC
'''

* Requirement 2 - Be Able to POST a New Blog Post


#   Flask Quick Start Documentation

#   Flask package on PyPi
https://pypi.org/project/Flask/

    *   Step1- Install Flask with pip
    > pip install -U Flask      (-U = upgrade)


    *   Step2- Create hello.py and run

    *   Step3- Create a Server

#   with 1.1.x
https://flask.palletsprojects.com/en/1.1.x/quickstart/

    MAQ:
    $ export FLASK_APP=hello.py

    Windows command:
    C:\path\to\app>set FLASK_APP=hello.py

    And on PowerShell:
    PS C:\path\to\app> $env:FLASK_APP = "hello.py"
    python -m flask run
    Running on //127.0.0.1:5000/


#   With 2.2.x
https://flask.palletsprojects.com/en/2.2.x/quickstart/

    PS C:\path\to\app> python -m flask --app hello run   (hello.py)

    -   To enable debug mode, use the --debug option.
    The server will automatically reload if code changes

    PS C:\path\to\app> python -m flask --app hello --debug run

    #   Windows Command Prompt Cheatsheet 
http://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf


#  Terminal Cheatsheet for Mac (Basics) 
https://github.com/appbrewery/terminal-mac-cheatsheet#english-version

#   Special Attributes built into Python
https://docs.python.org/3/library/stdtypes.html?highlight=__name__#special-attributes

#   __main__ — Top-level code environment
https://docs.python.org/3/library/__main__.html

#   Primer on Python Decorators
https://realpython.com/primer-on-python-decorators/

#   Measure Execution Time
https://ellibrodepython.com/tiempo-ejecucion-python

#   Rendering Templates- HTML files
https://flask.palletsprojects.com/en/2.2.x/quickstart/#rendering-templates

#   Rendering Templates- Static Files
https://flask.palletsprojects.com/en/2.2.x/quickstart/#static-files

#   HTML5 UP Website Template
https://html5up.net/

    for this example change:
    * Change assets/   ---> static/assets/  (css)
	* Change images/   ---> static/images   (images)

#   Update page .html from browser
    updte page ---> Developer Tools - console:
    > document.body.contentEditable=true
    true
    ...
    then 
    more tools  -save page as...
    (webpage, complete)

#   Beatiful Images
https://unsplash.com/

#   Jinja Documentation
https://jinja.palletsprojects.com/en/3.0.x/templates/

#   Jinja with APIs
https://genderize.io/
https://agify.io/

#   npoint Example Blog Data
https://www.npoint.io/docs/c790b4d5cab58020d391

#   Cretate Your Own Bin with npoint.io
https://www.npoint.io/docs/0100574fdac94e4b0831

# Flask GET, POST
https://www.w3schools.com/tags/att_form_method.asp

    Notice that the methods parameter accepts a list, so you can have multiple
    methods targeted by one route. e.g.
    @app.route("/contact", methods=["GET", "POST"])

    Flask has a method called request (don't confuse this with the requests module)
    which allows us to tap into the parameters of the request that was made to our
    server.

    More on this in the documentation here:
https://flask.palletsprojects.com/en/2.3.x/quickstart/#http-methods

https://flask.palletsprojects.com/en/2.3.x/quickstart/#the-request-object

#   Fix smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password 
    not accepted Gmail Python)
https://www.youtube.com/watch?v=jHP-9fXQGwo

#   ¿Cómo actualizar todos los paquetes de Python con pip?
https://www-w3docs-com.translate.goog/snippets/python/how-to-upgrade-all-python-packages-with-pip.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=rq#:~:text=You%20can%20use%20the%20pip,to%20the%20latest%20available%20versions.

    -pip list > all-list.txt (borrar encabezado y todos los numeros, dejar solo los nombres)

    -pip install -r all-list.txt --upgrade


#   Installing Flask-WTF
https://wtforms.readthedocs.io/en/3.0.x/

    The requirements.txt 
https://docs.google.com/document/d/e/2PACX-1vRIW_TuZ6z0ASjAoxgJgmzjGYLCDx019tKvphaTwK_Za7fnMKywUuXI0-s5wr0nQI_gprm6J6y7L9rL/pub


#   Creating Forms with Flask-WTF
https://flask-wtf.readthedocs.io/en/1.1.x/quickstart/
  

#   to create a secret key
https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key

# WTForms
https://wtforms.readthedocs.io/en/3.0.x/#help

# WTForms Validators
https://wtforms.readthedocs.io/en/3.0.x/validators/

#   Bootstrap Flask
https://bootstrap-flask.readthedocs.io/en/stable/

# render_form() function 
https://bootstrap-flask.readthedocs.io/en/latest/macros/#render-form

#   Create virtual env (python vscode)
    (terminal vscode) > python -m venv venv (venv= name virtual env)

#   Activate venv
    (terminal vscode)> venv\scripts\activate.bat (cmd)
    (terminal vscode)> venv\scripts\activate.ps1 (pwshell)
    Note: in pwshell ejecute like admin

    (terminal vscode) (env)> code\python\project1>

#   Install requirements.txt
    activate virtual env (or f1 python: select interpreter)
    (env)>code\python\project1> pip install -r requirements.txt

#   Quite a few SQL commands.
    SQLite es un sistema de gestión de bases de datos relacionales que se utiliza
    para almacenar y recuperar datos.
    https://www.codecademy.com/articles/sql-commands
    https://www.w3schools.com/sql/sql_ref_create_table.asp

#   SQLAlchemy
    SQLAlchemy es una biblioteca de Python que proporciona un mapeador
    objeto-relacional (ORM) para interactuar con bases de datos relacionales.

    https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/
    https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/#queries-for-views
    Flask-SQLAlchemy also has some handy extra query methods like
    get_or_404() that we can use. Since Flask-SQLAlchemy version 3.0 
    the previous query methods like Book.query.get() have been deprecated

* File generated for Copilot
Para que se utiliza en el contexto de SQLAlchemy  la declaracion Mapped y
cuando utilizarla?

En el contexto de SQLAlchemy, la declaración Mapped no es una parte estándar
de la sintaxis.

SQLAlchemy ofrece dos enfoques para definir modelos: el enfoque imperativo
(clásico) y el enfoque declarativo

1. Imperative Mapping (Clásico):
En este estilo, defines las tablas y columnas de la base de datos utilizando
funciones y clases de SQLAlchemy directamente en tu código.
Es más explícito y te da un mayor control sobre la estructura de la base de
datos.
Utilizas las funciones como Table, Column, ForeignKey, etc., para definir las
tablas y sus relaciones.
A menudo se utiliza cuando necesitas una personalización detallada o cuando
trabajas con bases de datos existentes con esquemas complejos.

-   Example: Imperative Mapping (Clásico)

from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import mapper

#- Configuración de la base de datos
metadata = MetaData()

#- Definición de la tabla 'movies'
user_table = Table(
    'tb_user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('fullname', String(50)),
    Column('nickname', String(12))
)

#- Mapeo imperativo de la clase User a la tabla 'tb_user'
mapper(User, user_table)


#- NOTA:
En el anterior código:

-* Hemos creado una instancia de MetaData llamada metadata.
-* Definimos la tabla tb_user con sus columnas correspondientes.
-* Utilizamos mapper(User, user_table) para mapear la clase User a la tabla
   tb_user


2. Declarative Mapping (Estilo Declarativo):
Este es el enfoque más común y moderno para definir mapeos en SQLAlchemy.
Implica definir una clase Python y utilizar funciones y decoradores especiales
de SQLAlchemy para definir las columnas, relaciones y otros metadatos de la
tabla.
Es simple, fácil de usar y permite definir los mapeos de manera clara y
concisa.
La mayoría de las aplicaciones modernas utilizan este estilo.
En el enfoque declarativo, defines tus modelos como clases Python que heredan
de db.Model. Esto facilita la creación y manipulación de tablas de base de
datos utilizando una sintaxis más intuitiva y orientada a objetos.

En resumen, no necesitas usar Mapped en tu código. En su lugar, utiliza la
palabra clave Column para definir las columnas de tu tabla. Aquí tienes un
ejemplo corregido de tu código:


-   Example: Declarative Mapping (Estilo Declarativo)

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

#- CREAR BASE DE DATOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

#- CREAR TABLA
class Movie(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(250), unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(String(500), nullable=False)
    rating = Column(Float, nullable=True)
    ranking = Column(Integer, nullable=True)
    review = Column(String(250), nullable=True)
    img_url = Column(String(250), nullable=False)

with app.app_context():
    db.create_all()


#- ###* complete program include class base *####

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

app = Flask(__name__)

#- Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

#- Clase Base para la herencia
class Base(db.Model):
    __abstract__ = True

#- Modelo de datos
class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(String(500), nullable=False)
    rating = Column(Float, nullable=True)
    ranking = Column(Integer, nullable=True)
    review = Column(String(250), nullable=True)
    img_url = Column(String(250), nullable=False)

#- Crear las tablas en la base de datos
with app.app_context():
    db.create_all()


#   pylint: disable=C0103
    Desactiva la advertencia C0103 de PyLint. Esta advertencia se emite cuando
    el nombre de una variable no cumple con el formato recomendado por PyLint.
    La directiva se coloca en la línea anterior a la que contiene el código que
    genera la advertencia.

#   API The Moviedb.org
https://developer.themoviedb.org/reference/search-movies       (search)
https://developers.themoviedb.org/3/movies/get-movie-details   (details)

#  Serialization
In order to do this, we have to turn our random_cafe SQLAlchemy Object into a JSON.
This process is called serialization.

Flask has a serialisation helper method built-in called jsonify() . But we have to
provide the structure of the JSON to return.
https://www.adamsmith.haus/python/docs/flask.jsonify

#   Postman
In VScode like extension.
The var location does not work, instead use loc

Documentation of Cafe & Wifi
https://documenter.getpostman.com/view/2568017/TVRhd9qR