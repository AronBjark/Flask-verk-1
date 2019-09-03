from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hallo heimur</h1><a href="/sida1"> sida 1 </a><a href="/sida2"> sida 2 </a><a href="/sida3"> sida 3 </a>'

@app.route('/sida1')
def sida1():
    return '<h1>sida 1</h1><a href="/"> sida 0 </a><a href="/sida2"> sida 2 </a><a href="/sida3"> sida 3 </a>'

@app.route('/sida2')
def sida2():
    return '<h1>sida 2</h1><a href="/"> sida 0 </a><a href="/sida1"> sida 1 </a><a href="/sida3"> sida 3 </a>'

@app.route('/sida3')
def sida3():
    return '<h1>sida 3</h1><a href="/"> sida 0 </a><a href="/sida1"> sida 1 </a><a href="/sida2"> sida 2 </a>'








if __name__ == "__main__":
	app.run(debug=True)