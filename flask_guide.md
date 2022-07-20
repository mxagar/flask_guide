# Flask Guide

These are my personal notes and examples on how to work with Flask for web development.

I created this repository following online tutorials and the Udemy course by José Portilla [Python and Flask Bootcamp: Create Websites using Flask](https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask).

Note that Python knowledge and some web development skills are required. For the latter, have a look at [jekyll_web_guide](https://github.com/mxagar/jekyll_web_guide) `/ html_css_bootstrap_guide.md`.

Mikel Sagardia, 2022.  
No guarantees.

### Table of Contents

1. [Flask Basics](#Flask-Basics)
2. [Templates](#Templates)
3. [Forms](#Forms)
4. SQL Databases
5. Large Applications
6. User Authentication
7. REST APIs
8. Deployment

# 1. Flask Basics

Installation:

```bash
# Select environment
conda activate ds
# Install if not done yet
conda install -c anaconda flask  -y
conda install -c anaconda flask-wtf  -y
```

## Hello World Example

`./examples/hello_world.py`:

```python
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

```

To run it:

```bash
cd examples/
python hello_world.py
# Open browser at http://127.0.0.1:5000/
# To finish web server: Ctrl+C
```

## Basic Routes

With `@app.route()` we define the name of the page we are creating:

```python
@app.route('/some_page') # http://127.0.0.1:5000/some_page
def index():
	return '<h1>Hello World!</h1>'
# We create:
# http://127.0.0.1:5000/some_page
# When deployed, the DNS is changed:
# http://my_domain.com/some_page

# We can create as many pages we want.
@app.route('/information') # http://127.0.0.1:5000/information
def info():
	return '<h1>Important info: ...</h1>'

# If we try to access a page that doesn't exist
# we get a 404 error: Not found
```

## Dynamic Routes

With dynamic routes we pass variables to the page functions. The effect is that we can type the matching URL address we want, i.e., we pass the variable name through the browser. Then, that variable is caught by the page function and it can process it as desired.

One possible application are custom user pages:

`./examples/dynamic_route.py`

```python
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

```

```bash
cd examples/
python dynamic_route.py
# Open browser at http://127.0.0.1:5000/
# http://127.0.0.1:5000/information
# http://127.0.0.1:5000/user/mikel -> check that content is modified with MIKEL
# To finish web server: Ctrl+C
```

## Debug Mode

We can activate debug mode in the application as follows:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

That way, if we have an error in any of the page functions, instead of displaying an "Internal Server Error" page, we get a traceback list of all the steps until the first error.

We can also open an interactive python debugging console clicking on the traceback step icon for that; but **we need a PIN**. The PIN is displayed on the terminal/shell when we run the python script.

NOTE: debug mode should be deactivated when we deploy to production!


# 2. Templates


# 3. Forms


# 4. SQL Databases


# 5. Large Applications


# 6. User Authentication


# 7. REST APIs


# 8. Deployment


