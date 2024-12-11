from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User

from . import db
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)
@auth.route('/home',)
def home():
    return render_template("home.html", user=current_user)
@auth.route('/contact',)
def contact():
    return render_template("contact.html", user=current_user)
@auth.route('/aboutus',)
def aboutus():
    return render_template("aboutus.html", user=current_user)
