from flask import Flask

app = Flask(__name__)

from auto_support.core.views import core

app.register_blueprint(core)