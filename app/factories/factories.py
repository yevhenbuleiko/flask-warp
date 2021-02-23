
__all__ = ('blueprints_factory')

def blueprints_factory(app, blueprints):
	''' Configure bluepritns '''
	for blueprint in blueprints:
		app.register_blueprint(blueprint)