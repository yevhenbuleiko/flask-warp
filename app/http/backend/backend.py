from flask import Blueprint
from app.http.backend.factories import view_factory
from app.utils.config import get_config

__all__ = ('backend')

def backend():
	backend = Blueprint('backend', __name__, url_prefix='/', \
		template_folder="templates")
	view_factory(backend)
	return backend