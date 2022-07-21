# Run: python flash.py

from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

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
class SimpleForm(FlaskForm):
    # The form has just one button
    submit = SubmitField('Click Me.')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        # This is the flash alert message        
        flash("You just clicked the button!")

        # We redirect here, but the flash alert has been instantiated
        return redirect(url_for('index'))

    return render_template('flash-home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
