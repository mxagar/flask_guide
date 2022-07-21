# Flask Guide

These are my personal notes and examples on how to work with Flask for web development.

I created this repository following online tutorials and the Udemy course by José Portilla [Python and Flask Bootcamp: Create Websites using Flask](https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask).

Note that Python knowledge and some web development skills are required. For the latter, have a look at [jekyll_web_guide](https://github.com/mxagar/jekyll_web_guide) `/ html_css_bootstrap_guide.md`.

Mikel Sagardia, 2022.  
No guarantees.

### Table of Contents

1. [Flask Basics](#Flask-Basics)
    - Hello World Example
    - Basic Routes
    - Dynamic Routes
    - Debug Mode
2. [Templates](#Templates)
3. [Forms](#Forms)
4. SQL Databases
5. Large Applications
6. User Authentication
7. REST APIs
8. Deployment

There is an `examples/` folder with the examples described in the current guide.

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

`./examples/01_basics/hello_world.py`:

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

`./examples/01_basics/dynamic_route.py`

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

Instead of returning HTML strings, we usually render a template HTML file. These are **templates** and they are rendered with the function `render_template(html_filepath)`.

Templates need to be located in a folder called `templates/` and they can use resources from other locations, e.g., image files.

## Basic Template

All the HTML template files need to be in `templates/`. The resources they use can be anywhere, e.g., in this case, they are in the folder `static/`.

Basic example in `./examples/02_templates`.

`templates/basic-template.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Basic</title>
  </head>
  <body>
    <h1>Hello!</h1>
    <h2>Here is a cute picture of a puppy!</h2>
    <!-- The image can be located anywhere, but the HTML file in templates/-->
    <img src="../static/puppy_pic.jpg" width="600" height="400">

  </body>
</html>

```

`basic_template.py`:

```python
# Run: python basic_template.py

# Import the render_template function
from flask import Flask, render_template
app = Flask(__name__)

# Render an HTML template file
# All templates are located in the folder templates (Flask looks for that name)
# This template uses an image in the folder static
# The folder name with the resources is arbitrary
@app.route('/')
def index():
    # Connecting to a template (html file)
    return render_template('basic-template.html')

# Debug mode active; deactivate to go to production
if __name__ == '__main__':
    app.run(debug=True)

```

## Template Variables with Jinja

We can use [Jinja templating](https://jinja.palletsprojects.com/en/3.1.x/), as in Jekyll, to inject variables from the python script in the HTML document visualized with `render_template()`; simply, the variables are created inside the page function and passed directly to `render_template()`. Then, we access them with Jinja notation in the HTML document. We can pass strings, lists, dictionaries, etc.

Jinja command lines are of 3 types:

- `{{ ... }}`: variables and filters
- `{% ... %}`: control flow
- `{# ... #}`: comments

Basic example in `./examples/02_templates`.

`variables.py`

```python
# Run: python variables.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # Pass in a puppy name
    # We insert it to the html with jinja2 templates!
    return '<h1> Go to /puppy/name </h1>'

@app.route('/puppy/<name>')
def adv_puppy_name(name):
    # Pass in a puppy name
    # We insert it to the html with Jinja templates!
    message = "Trying variables."
    letters = list(name)
    pup_dict = {'pup_name':name}
    return render_template('variables-template.html',
                           message=message,
                           name=name,
                           mylist=letters,
                           mydict=pup_dict)

if __name__ == '__main__':
    app.run(debug=True)
```

`templates/variables-template.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Basic</title>
  </head>
  <body>
    <!-- The message is defined in render_template() and passed to the HTML -->
    <h1>{{message}}</h1>
    <!-- name is passed via the browser to the python script and from there to he HTML via render_template() -->
    <h1>Basic variable insert: {{name}}!</h1>
    <!-- Recall that we set mylist=letters in the .py file. -->
    <!-- You could use whatever variable names you want -->
    <h1>List example: {{mylist}}</h1>
    <!-- We can index the list as well -->
    <h1>Indexing the list for the first letter: {{mylist[0]}}</h1>
    <!-- We can also use dictionaries -->
    <h1>Puppy name from dictionary: {{mydict['pup_name']}}</h1>
  </body>
</html>
```

## Template Control Flow with Jinja

While with Jinja variables we use `{{ variable }}` within the HTML text, we need to use `{% ... %}` for control flow statements, i.e., `if, for`, etc. Inside them, we can access the variables.

Examples:

```html
<ul>
    {% for item in mylist %}
    <li>{{ item }}</li>
    {% endfor %}
</ul>

{% if username == "Mikel" %}
    <h1>Insert credit card number.</h1>
{% elif username == "Unai" %}
    <h1>Ask your parents.</h1>
{% else %}
    <h1>You're not authenticated.</h1>
{% endif %}
```

Example in the `examples/` folder:

`control_flow.py`:

```python
# Run: python control_flow.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    puppies = ['Fluffy','Rufus','Spike']
    return render_template('control-flow-template.html',
                           puppies=puppies)

if __name__ == '__main__':
    app.run(debug=True)
```

`templates/control-flow-template.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <p>Here we use a for loop for a list</p>
    <ul>
      {% for pup in puppies %}
      <li>{{pup}}</li>
      {% endfor %}
    </ul>
    <p>We can also add if/else statements:</p>
    {% if 'Rufus' in puppies %}
      <p>Found you in the list of puppies Rufus!</p>
    {% else %}
      <p>Hmm, Rufus isn't in this list.</p>
    {% endif %}
  </body>
</html>
```

## Template Inheritance and Filters

### Inheritance

The idea is to define a base HTML template file which is inherited by other HTML files. That way, we don't need to repeat ourselves with common elements like styles, menu bars, etc.

This is accomplished with `{% extends "base.html" %}` and `{% block content %}`:

- We set `{% block content %} {% endblock %}` in the base HTML where the concrete content would go in the inherited page.
- The inherited page contains `{% extends "base.html" %}` and after it its concrete content wrapped in `{% block content %} CONTENT {% endblock %}`.

Note that the name of the block `content` is arbitrary, but must match between the files; additionally, we can use several blocks.

![Template Inheritance](./pics/template_inheritance.png)

### Filters

Filtering consists in applying functions to variables; often these function names are similar to the ones in python:

```
{{ variable | filter }}
{{ name | capitalize }}
```

We could perform these actions in python, but we have the flexibility of doing it on the HTML code.

Important links on filter:

- [Template Designer Documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/)
- [List of built-in filters](https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters)

### `url_for()`

Instead of using hard-coded HTML filepaths we can use `url_for()` in a Jinja command: we enter the page function name and the associated HTML file path is returned.

For instance, if we have this python app:

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def about_page_function():
    return render_template('/path/to/about.html')
```

Then, in any HTML file we have access to the complete `about.html` file path via its **page function name**:

```html
{{ url_for('about_page_function') }}
```

We can also access any asset or file, not only HTML files. In that case, we specify the folder name and the file name:

```html
{{ url_for('static', filename='pic.jpg') }}
```

### Example

This example is in `examples/02_templates/`.

Notes:

- The consists of 1 python file and 3 HTML files; one HTML is the base which is inherited.
- Variable filtering is used: `{{ name | capitalize }}`
- We use `url_for()` to get an HTML filepath and a pic filepath.

```python
# Run: python inheritance.py

from flask import Flask, render_template
app = Flask(__name__)

# Home page
# The HTML file inherits from inheritance-base.html
# which contains a common Bootstrap nav-bar
@app.route('/')
def index():
    return render_template('inheritance-home.html')

# Puppy name page
# The HTML file inherits from inheritance-base.html
# which contains a common Bootstrap nav-bar
@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('inheritance-puppy.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- inheritance-base.html -->

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Puppy Rock</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="{{ url_for('index') }}">Puppies Rock!</a>
    </nav>
    {% block content %}
    {% endblock %}
  </body>
</html>

<!-- inheritance-home.html -->

{% extends "inheritance-base.html"%}
{% block content %}
<h1>This is the home page.</h1>
<h2>Go to /puppy/name</h2>
{% endblock %}

<!-- inheritance-puppy.html -->

{% extends "inheritance-base.html"%}
{% block content %}
<h1>This is the page for the puppy: {{ name | capitalize }}.</h1>
<a href="{{ url_for('static',filename='puppy_pic.jpg') }}">Click here for a picture of {{ name | capitalize }}.</a> 
{% endblock %}

```

## Template Forms, Catching Field Values and Error Pages

In this section, a website with several pages is created; they direct to a sign-up form from Bootstrap. After signing up, a thank you page with the signed name is shown. However, that information is not saved anywhere.

New learned things:

- How to get values of fields filled into a form with `request`. We can access what the user inserts in `input` fields like `<input type="text" name="first">` from anywhere in the python script using the name of the field
- Error page: basically a custom page is defined with the decorator `@app.errorhandler(404)`.

The example is in `examples/02_temaplates`.

```python
# Run: python form.py

# Note we imported request!
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form-index.html')

# This page will have the sign up form.
# The user inserts values into form fields.
# These values are accessible via request.args.get(),
# as shown in the next page function.
# However, note that in this example we do not persist the values.
@app.route('/signup_form')
def signup_form():
    return render_template('form-sign-up.html')

# This page will be the page after the form
@app.route('/thankyou')
def thank_you():
    # We can access what the user inserts in `input` fields like
    # `<input type="text" name="first">`
    # from anywhere in the python script using the name of the field
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('form-thankyou.html',first=first,last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('form-404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

```

```html
<!-- form-base.html -->

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Puppy Rock</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="{{url_for('index')}}">Home Page</a>
    </nav>
    {% block content %}
    {% endblock %}
  </body>
</html>

<!-- form-index.html -->

{% extends "form-base.html"%}
{% block content %}
<div class="jumbotron">
<p>Welcome to Puppy Rock!</p>
<p>Wanna sign up for our puppy band?</p>
<a href="{{url_for('signup_form')}}">Sign up for auditions here</a>
</div>
{% endblock %}

<!-- form-sign-up.html -->

{% extends "form-base.html"%}
{% block content %}
<div class="jumbotron">
    <h1>Welcome to the sign up page!</h1>
    <p>We're excited to have you audition for our band</p>
    <p>This will redirect to a thank you page.</p>
    <p>
      Please note, we're just puppies, so we haven't
      learned how to save your information yet!
    </p>
    <form action="{{url_for('thank_you')}}">
        <label for="first">First Name</label>
        <input type="text" name="first">
        <label for="last">Last Name</label>
        <input type="text" name="last">
        <input type="submit" value="Submit Form">
    </form>
</div>
{% endblock %}

<!-- form-thankyou.html -->

{% extends "form-base.html"%}
{% block content %}
<div class="jumbotron">

  <h1>Thank you for signing up {{first}} {{last}}!</h1>
</div>
{% endblock %}

<!-- form-404.html -->

{% extends "form-base.html"%}
{% block content %}
<div class="jumbotron">
<p>Sorry, we couldn't find the page you were looking for.</p>
<p>Cut us some slack, we're just puppies!</p>
</div>
{% endblock %}

```


# 3. Forms


# 4. SQL Databases


# 5. Large Applications


# 6. User Authentication


# 7. REST APIs


# 8. Deployment


