from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

# Blueprints allow to have an 'add' view for several modules/tables
# We'll see this view in the navigation bar as:
# http://127.0.0.1:5000/owners/add
# But for that, we need to register the blueprint in the __init__.py
owners_blueprint = Blueprint('owners',
                              __name__,
                              template_folder='templates/owners')

# Instead of add.route(), we use the blueprint we just created
@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        # Add new owner to database
        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        # Note the redirection is different now: puppies.list
        return redirect(url_for('puppies.list'))
        
    return render_template('add_owner.html',form=form)
