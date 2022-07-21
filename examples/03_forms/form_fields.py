# Run: python form_fields.py

# The session dictionary makes possible to store information
# visible to the whole application while the user is interacting in a session 
from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
# We can import many fields, there's one for each HTML form component
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField, SelectField, TextField,
                     TextAreaField, SubmitField)
# We can import field validators too!
from wtforms.validators import DataRequired

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
    # We can pass the validators of a field we'd like
    breed = StringField('What breed are you?',validators=[DataRequired()])
    neutered  = BooleanField("Have you been neutered?")
    # Every time we define dictionaries or tuples in the field definition
    # the user sees the value (Happy), but we get the key (mood_one).
    mood = RadioField('Please choose your mood:',
                      choices=[('mood_one','Happy'),('mood_two','Excited')])
    # In some OS we need unicode strings for field selection, thus we use u
    food_choice = SelectField(u'Pick Your Favorite Food:',
                              choices=[('chi', 'Chicken'),
                                       ('bf', 'Beef'),
                                       ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

# We define the methods GET and POST
# so that we can read/write from fields
@app.route('/', methods=['GET', 'POST'])
def index():
    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.
        # We use the session dictionary, which lives on the server
        # and is accessible for the complete application
        # while the user is interacting with the form/page in a session,
        # then it's reset.
        # We can extend the session dictionary with our desired fields.
        # Recall the notation: form.<field>.data
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        # When form correctly filled in, show thank you page
        return redirect(url_for('thankyou'))

    # Original return to show unfilled form
    return render_template('fields-home.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('fields-thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
