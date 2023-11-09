from flask import Flask, request
from flask import Blueprint, render_template

import csv
import time
import hashlib

app = Flask(__name__)

def get_secret_code():
    return "7GTgk3dtR7U@wCAH"

def get_real_password_from_db(user):
    with open('user_db2.csv') as inf:
        reader = csv.DictReader(inf)
        for row in reader:
            if row['username'] == user:
                return row['password']
    return False


@app.route("/")
def hello_world():
        return "<p>Hello, World!</p>"


@app.route("/login", methods=['POST'])
def login_post():
    user = hashlib.sha256(request.form.get('user').encode('utf-8')).hexdigest() #Also want to hash username to prevent leaking users
    password = hashlib.sha256(request.form.get('password').encode('utf-8')).hexdigest() #Good steward of passwords by comparing hashes

    real_password = get_real_password_from_db(user)

    start_time = time.time()

    if real_password and real_password == password:
        time.sleep(1 - (time.time() - start_time)) #Fixed response time of 1 second to avoid side channel
        return get_secret_code()
    else:
        time.sleep(1 - (time.time() - start_time))
        return "Invalid Credentials\n" #Always return same error message whether or not user exists

    #     for i in range(0, len(real_password)):
    #         if (i >= len(password)) or (password[i] != real_password[i]):
    #             return "Invalid Credentials\n"
    #         # This is here to things a little easier on you
    #         # We could make this work without it, but it would be unpleasant
    #         #time.sleep(0.01)
    #
    #     return get_secret_code()
    # else:
    #     return "Invalid Credentials\n"
    
    ### THERE SHOULD BE THE SAME RETURN MESSAGE FOR INVALID USER AND INVALID PASSWORD
    ### CHECK THE WHOLE PASSWORD AT ONCE, OR SLEEP FOR SOME VARIABLE AMOUNT OF TIME TO MAKE THE OVERALL RESPONSE TIME CONSTANT
    ### USE HASHES OF BOTH THE REAL PWD AND USER INPUT FOR COMPARISON INSTEAD OF USING THEM IN PLAINTEXT