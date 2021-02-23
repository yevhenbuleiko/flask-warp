from flask import ( Blueprint, render_template, )
from app.http.frontend.factories import view_factory
from jinja2 import TemplateNotFound

__all__ = ('frontend')

def frontend():
	frontend = Blueprint('frontend', __name__, url_prefix='/', template_folder="templates")
	view_factory(frontend)
	''' test ''' 
	# @frontend.route('/test_template')
	# def test():
	# 	try:
	# 		return render_template('frontend/test.html', title="Test Page", message="First template test page !!!")
	# 	except TemplateNotFound:
	# 		return 'Error in test method'
	''' ***  '''
	return frontend