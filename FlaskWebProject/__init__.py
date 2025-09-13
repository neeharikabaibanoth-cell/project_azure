"""
The flask application package.

import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.logger.setLevel(logging.INFO)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views"""

import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# Setup session
Session(app)

# Setup database
db = SQLAlchemy(app)

# Setup login manager
login = LoginManager(app)
login.login_view = 'login'

# Setup logging
if not app.debug and not app.testing:
    # Create logs directory if not exists
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    # Rotating file handler - keeps logs under 1MB each, with backup count
    file_handler = RotatingFileHandler('logs/flaskapp.log', maxBytes=1024 * 1024, backupCount=10)
    file_handler.setLevel(logging.WARNING)  # Logs warnings and above
    
    # Log message format
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )
    file_handler.setFormatter(formatter)
    
    # Add the handler to the app's logger
    app.logger.addHandler(file_handler)

# Set the default logger level (can be INFO or WARNING)
app.logger.setLevel(logging.INFO)

import FlaskWebProject.views

