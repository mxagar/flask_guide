from flask import Flask
app = Flask(__name__) # __name__ is __main__

# We pass to the instantiated Flask app
# the pages we want in the rout we like
# Here: an index page function located in the root
@app.route('/')
def index():
	# In this case, we directly return HTML code
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()
