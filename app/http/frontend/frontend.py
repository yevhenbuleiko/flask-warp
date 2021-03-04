from flask import ( Blueprint, render_template, )
from app.http.frontend.factories import view_factory
from jinja2 import TemplateNotFound

from app.utils.config import get_config

__all__ = ('frontend')

def frontend():
	frontend = Blueprint('frontend', __name__, url_prefix='/', \
		template_folder="templates")
	view_factory(frontend)
	''' test ''' 
	@frontend.route('/test_template')
	def test():
		try:
			get_config_message = get_config('settings.SETTINGS_TEST_VALUE')
			return render_template('frontend/test.html', \
				title="Test Page", \
				message="First template test page !!!", \
				confmsg=get_config_message)
		except TemplateNotFound:
			return 'Error in test method'
	''' ***  '''
	return frontend