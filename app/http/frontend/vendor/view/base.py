from app.vendor.view import BaseView

__all__ = ('FrontendBaseView')

class FrontendBaseView(BaseView):
	''' Base class for frontend view '''
	# Base route for frontend pages
	route_base = '/'

	# initialize
	def __init__(self):
		# Template frontend prefix
		self.templ_prefix = 'frontend'

	# before each request
	def before_request(self, name):
		super(FrontendBaseView, self).before_request(name)
	# After each request
	def after_request(self, name, response):
		super(FrontendBaseView, self).after_request(name, response)
		return response

