from app.http.frontend.vendor.view import FrontendBaseView
from flask_classy import route
from flask import (render_template, g, request, url_for, current_app, send_from_directory, json, redirect, make_response, abort)

__all__ = ('HomeView')

class HomeView(FrontendBaseView):
	''' Class Home View '''

	def __init__(self):
		super(HomeView, self).__init__()

	def before_request(self, name):
		super(HomeView, self).before_request(name)

	def after_request(self, name, response):
		super(HomeView, self).after_request(name, response)
		return response

	@route('/home')
	def home(self):
		self.template = '/home/home.html'
		self.pageTitle = current_app.config['APP_NAME']
		self.ctx['message'] = 'Flask-Warp Home Page'
		return self.render_out()