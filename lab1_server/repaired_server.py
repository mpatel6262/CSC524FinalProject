
from flask import Flask, request
from flask import Blueprint, render_template

import csv
import time
import hashlib

app = Flask(__name__)

def get_secret_code():
    return "7GTgk3dtR7U@wCAH"

def get_real_password_from_db(user):
    ret = False
    with open('user_db2.csv') as inf:
        reader = csv.DictReader(inf)
        for row in reader:
            if row['username'] == user:
                ret = row['password']
    return ret


@app.route("/")
def hello_world():
        return "<p>Hello, World!</p>"


@app.route("/login", methods=['POST'])
def login_post():
    user = hashlib.sha256(request.form.get('user').encode('utf-8')).hexdigest()
    password = hashlib.sha256(request.form.get('password').encode('utf-8')).hexdigest() #Good steward of passwords by comparing hashes 

    hashed_password = get_real_password_from_db(user)

    if hashed_password and hashed_password == password:
        return get_secret_code()
    return "Invalid Credentials\n"