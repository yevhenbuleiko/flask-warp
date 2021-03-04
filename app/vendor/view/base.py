from flask_classy import FlaskView
from flask import (render_template, g, abort, request, url_for, )

__all__ = ('BaseView')

class BaseView(FlaskView):
	''' Base class for all views classes '''
	# Prefix for all routes
	route_prefix = '/'
	# Page title
	pageTitle = ''
	# Template prefix
	templ_prefix = ''
	# Template file name
	template = ''
	# Data
	ctx = {}

	# Before each request
	def before_request(self, name):
		pass
	# After each request
	def after_request(self, name, response):
		return response

	# Render template with data from ctx directory
	def render_out(self):
		self.ctx['title'] = self.pageTitle
		return render_template(self.templ_prefix+self.template, **self.ctx)
		