from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/resume')
def resume():
    return render_template('resume.html')

@main.route('/projects')
def projects():
    return render_template('projects.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')