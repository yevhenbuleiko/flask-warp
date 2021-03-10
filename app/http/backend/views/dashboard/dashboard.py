from app.http.backend.vendor.view import BackendBaseView
from flask_classy import route
from flask import (render_template, g, request, url_for, current_app, 
	send_from_directory, json, redirect, make_response, abort, )

__all__ = ('AdminDashboardView')

class AdminDashboardView(BackendBaseView):
	''' Class Admin Dasboard View '''

	def __init__(self):
		super(AdminDashboardView, self).__init__()

	def before_request(self, name):
		super(AdminDashboardView, self).before_request(name)

	def after_request(self, name, response):
		super(AdminDashboardView, self).after_request(name, response)
		return response

	@route('/dashboard')
	def home(self):
		self.template = '/dashboard/dashboard.html'
		self.pageTitle = current_app.config['APP_NAME'] + '(Dashboard)'
		self.ctx['message'] = 'Flask-Warp Dashboard Page'
		return self.render_out()