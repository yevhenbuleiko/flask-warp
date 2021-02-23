from flask import Flask 
from app.factories import blueprints_factory
# Import Blueprints
from app.http.frontend import frontend

__all__ = ('create_app')

# List Of Blueprints
blueprints = ( frontend(), )

def create_app():
	app = Flask(__name__)
	blueprints_factory(app, blueprints)
	return app 
