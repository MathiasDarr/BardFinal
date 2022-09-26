from flask import Blueprint, request
import logging

log = logging.getLogger('werkzeug')
api = Blueprint('auth_api', __name__)


@api.route('/auth/init')
def auth_init():
    request.referrer
