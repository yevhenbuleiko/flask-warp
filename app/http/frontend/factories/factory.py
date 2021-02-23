from app.http.frontend.views.home import HomeView

def view_factory(frontend):
	''' Register frontend view classes '''
	HomeView.register(frontend)