from app.vendor.view import BaseView

__all__ = ('BackendBaseView')

class BackendBaseView(BaseView):
	''' Base class for backend view '''
	# Base route for backend pages
	route_base = '/admin/'

	# initialize
	def __init__(self):
		# Template frontend prefix
		self.templ_prefix = 'backend'

	# before each request
	def before_request(self, name):
		super(BackendBaseView, self).before_request(name)
	# After each request
	def after_request(self, name, response):
		super(BackendBaseView, self).after_request(name, response)
		return response