from flask import Flask 
from app.helpers import dict_from_yaml_file
from app.factories import ( blueprints_factory, config_factory, )
# Import Blueprints
from app.http.frontend import frontend
from app.http.error import error

__all__ = ('create_app')

# List Of Blueprints
blueprints = ( frontend(), error(), )

def create_app(config_file=None):
	app = Flask(__name__)
	# Load Config Values From File
	config_from_file = dict_from_yaml_file(config_file)
	# Setup App
	config_factory(app, config_from_file)
	blueprints_factory(app, blueprints)
	return app 
