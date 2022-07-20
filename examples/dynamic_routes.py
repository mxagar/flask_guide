from flask import Flask
app = Flask(__name__)

# Main page
@app.route('/') # http://127.0.0.1:5000
def index():
    return '<h1>Hello World!</h1>'

# We can add as many pages we want with route.
@app.route('/information') # http://127.0.0.1:5000/information
def info():
    return '<h1>About page</h1>'

# Dynamic routing: we pass a variable that changes the URL name
# The idea is that the page is created when we enter the address,
# i.e., we pass the variable via the web browser!
# Then, that variable can be processed in the page function.
# http://127.0.0.1:5000/user/mikel -> URL accepted and content modified
# http://127.0.0.1:5000/user/unai -> URL accepted and content modified
# We can apply changes to name: name.upper(), etc.
@app.route('/user/<name>') 
def puppy(name):
    # Page for an individual puppy.
    return '<h1>This is a page for {}<h1>'.format(name.upper())

if __name__ == '__main__':
    app.run()
