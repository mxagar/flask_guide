# Run: python basic_form.py

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

# Configure a secret SECRET_KEY in the app config dictionary.
# Here, we do it explicitly in the code for learning
# but we NEVER should do that.
# An alternative is to define it as an environment variable
# and to catch it: os.environ['VARIABLE']
app.config['SECRET_KEY'] = 'mysecretkey'

# Now create a WTForm Class
# Lots of fields available:
# https://wtforms.readthedocs.io/en/3.0.x/fields/
class InfoForm(FlaskForm):
    '''This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    breed = StringField('What breed are you?')
    submit = SubmitField('Submit')

# We need to pass the methods GET and POST
# to interact with the HTML form from python
@app.route('/', methods=['GET', 'POST'])
def index():
    # Set the breed to a boolean False
    # so we can use it in an if statement in the HTML.
    breed = False
    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (see validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form: GET
        # Note the notation: form.<field>.data
        breed = form.breed.data
        # Reset the form's breed data to be False: POST
        form.breed.data = ''
    # We need to pass all the objects we interact with
    return render_template('basic-home.html', form=form, breed=breed)

if __name__ == '__main__':
    app.run(debug=True)
