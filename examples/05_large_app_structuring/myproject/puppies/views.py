from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.puppies.forms import AddForm, DelForm
from myproject.models import Puppy

# Blueprints allow to have an 'add' view for several modules/tables
# We'll see this view in the navigation bar as:
# http://127.0.0.1:5000/puppies/add
# http://127.0.0.1:5000/puppies/list
# http://127.0.0.1:5000/puppies/delete
# But for that, we need to register the blueprint in the __init__.py
puppies_blueprint = Blueprint('puppies',
                              __name__,
                              template_folder='templates/puppies')

# Instead of add.route(), we use the blueprint we just created
@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Puppy to database
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('add.html',form=form)

# Instead of add.route(), we use the blueprint we just created
@puppies_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()

    return render_template('list.html', puppies=puppies)

# Instead of add.route(), we use the blueprint we just created
@puppies_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('delete.html',form=form)
