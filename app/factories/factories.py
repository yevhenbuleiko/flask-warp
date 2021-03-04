from app.utils.config import make_config

__all__ = ('blueprints_factory')

def blueprints_factory(app, blueprints):
	''' Configure bluepritns '''
	for blueprint in blueprints:
		app.register_blueprint(blueprint)

def config_factory(app, config_from_file: dict):
	''' Configure App Configuration '''
	app.config.update(make_config(config_from_file))