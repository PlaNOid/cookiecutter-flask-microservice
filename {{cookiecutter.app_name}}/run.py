import logging
import subprocess
from IPython import embed
from flask import url_for, abort
from flasgger import Swagger
from webargs.flaskparser import parser
from flask_builder import create_app, create_db, is_db_exists, drop_db, init_app, init_mail
from lib.utils import ApiException, find_models_and_tables, ujsonify, module_generator

from cookiecutter.main import cookiecutter
from cookiecutter.exceptions import OutputDirExistsException
from config import MODULE_TEMPLATE_REPO


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S'
)


app = create_app(name='{{cookiecutter.app_name}}')
init_app(app)

{% if cookiecutter.use_mail == 'y' %}
init_mail(app)
{% endif %}

app.register_error_handler(ApiException, lambda err: err.to_result())


app.config['SWAGGER'] = {
    'title': '{{cookiecutter.full_app_name}} API',
    'uiversion': 2,
    'description': '{{cookiecutter.project_short_description}}',
    'termsOfService': ''
}
swagger = Swagger(app)


@parser.error_handler
def handle_parse_error(error, request):
    response = ujsonify(**error.messages)
    response.status_code = 400
    abort(response)


@app.cli.command()
def init():
    """Creates all tables, admin and so on if needed"""
    dsn = app.config.get('SQLALCHEMY_DATABASE_URI')
    if dsn:
        if not is_db_exists(dsn):
            create_db(dsn)


@app.cli.command()
def drop_all():
    """Drop and recreates all tables"""
    dsn = app.config.get('SQLALCHEMY_DATABASE_URI')
    if dsn and input('Do you want to DROP DATABASE:%s ?!' % dsn):
        drop_db(dsn)


@app.cli.command()
def debug():
    """Runs the shell with own context and ipython"""
    import re
    import os
    from pprintpp import pprint as p

    shell_context = locals()
    shell_context.update(find_models_and_tables())

    embed(user_ns=shell_context)


@app.cli.command()
def dbshell():
    connect_args = app.db.engine.url.translate_connect_args()
    connect_url = "postgresql://{username}:{password}@{host}:{port}/{database}".format(**connect_args)
    subprocess.call(['pgcli', connect_url])


@app.cli.command()
def routes():
    """ List all avalable routes """
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


@app.cli.command()
def addmodule():
    name = input('module name: ').lower()
    context = {
        'module_name': name,
        'module_upper_name': name.upper(),
        'model_name': name.capitalize()

    }
    status = f'module {name} is created'
    try:
        cookiecutter(MODULE_TEMPLATE_REPO, no_input=True, extra_context=context, output_dir='./app')
    except OutputDirExistsException:
        status = f'module {name} already exists'
    print(status)

    
if __name__ == '__main__':
    app.run()
