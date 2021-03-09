from flask import ( Blueprint, render_template, )

_all__ = ('error')

def error():
	error = Blueprint('error', __name__, url_prefix='/error/', template_folder="templates")

	@error.app_errorhandler(403)
	def forbidden_page(error):
		return render_template("error/403.html", desc="Forbidden page"), 403

	@error.app_errorhandler(404)
	def not_found_error(error):
		return render_template('error/404.html', desc="Page not found"), 404

	@error.app_errorhandler(405)
	def method_not_allowed(error):
		return render_template("error/405.html", desc="Call wrong method"), 404

	@error.app_errorhandler(500)
	def internal_error(error):
		return render_template('error/500.html', desc="Server error"), 500
	
	return error