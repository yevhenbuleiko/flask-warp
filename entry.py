from app import create_app

app = create_app()

''' test '''
@app.route('/')
def hello_world():
	return 'Hello world!'
''' *** '''

if __name__=='__main__':
	app.run(host='127.0.0.1', port='4001')