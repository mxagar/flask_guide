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
