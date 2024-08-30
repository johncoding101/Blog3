# -*- coding: utf-8 -*-
'''
Created on Monday Aug 19 20:16:10 2024
Udemy -100 Days of code (Angela Yu)
video -468 Requirement 2 - Be Able to POST a New Blog Post
Author: JohnC
'''

# * Requirement 2 - Be Able to POST a New Blog Post

from datetime import date
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField, CKEditor


# Make sure the required packages are installed:
# Open the Terminal in PyCharm (bottom left).
# On Windows type:
# python -m pip install -r requirements.txt
# On MacOS type:
# pip3 install -r requirements.txt
# This will install the packages from the requirements.txt for this project.


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)  # * init ckeditor
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    """_summary_

    Args:
        DeclarativeBase (_type_): _description_
    """
    # pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    """_summary_

    Args:
        db (_type_): _description_
    """
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# WTForm
class CreatePostForm(FlaskForm):
    """_summary_

    Args:
        FlaskForm (_type_): _description_
    """
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    """_summary_

    Returns:
        _type_: _description_
    """
    # * Query the database for all the posts.
    # *Convert the data to a python list.
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)
    # posts = []
    # return render_template("index.html", all_posts=posts)


# *Add a route so that you can click on individual posts.
# @app.route('/')
@app.route("/post/<int:post_id>")
def show_post(post_id):
    """_summary_

    Args:
        post_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    # * Retrieve a BlogPost from the database based on the post_id
    # requested_post = "Grab the post from your database"
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# * add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    """_summary_

    Returns:
        _type_: _description_
    """
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template("about.html")


@app.route("/contact")
def contact():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
