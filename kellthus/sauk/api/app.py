from flask import Flask
from flask_cors import CORS
from logging.handlers import RotatingFileHandler
import logging
import os
import sys

from api.views import mount_blueprints

def create_app():
    app = Flask(__name__)
    enviornment = 'dev'
    CORS(
        app,
        supports_credentials=True,
        origins=["localhost:3000"]
    )
    mount_blueprints(app)
    setup_logging(enviornment)
    return app


def setup_logging(flask_env):
    logFormatter = logging.Formatter("%(asctime)s")
    log = logging.getLogger('werkzeug')
    if flask_env == 'development':
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.WARN)
    log.propagate = False
    if len(log.handlers) < 1:
        streamHandler = logging.StreamHandler(sys.stdout)
        streamHandler.setFormatter(logFormatter)
        log.addHandler(streamHandler)
    else:
        streamHandler = log.handlers[0]
        streamHandler.setFormatter(logFormatter)
    if not os.path.isdir('logs'):
        os.mkdir('logs')

    fileHandler = RotatingFileHandler("logs/app.log", maxBytes=500000)
    fileHandler.setFormatter(logFormatter)
    log.addHandler(fileHandler)
