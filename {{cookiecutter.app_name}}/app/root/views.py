from flask import Blueprint

mod = Blueprint('root', __name__)


@mod.route('/')
def root_view():
    return 'Hello world!'




