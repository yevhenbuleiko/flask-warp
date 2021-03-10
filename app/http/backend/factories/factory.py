from app.http.backend.views.dashboard import AdminDashboardView

def view_factory(backend):
	''' Register backend view classes '''
	AdminDashboardView.register(backend)