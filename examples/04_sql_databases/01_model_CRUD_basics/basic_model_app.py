import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

### -- SET UP OUR SQLite DATABASE

# This grabs our directory, OS independent
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Connect our Flask App to our Database.
# We specify the file in which the database is saved.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# We can track all the modifications done to the database
# but we deactivate it.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db is the database, which knows the Flask app
# using db we create models/tables to it,
# which are composed by rows.
db = SQLAlchemy(app)

# Add on migration capabilities in order to run terminal commands
Migrate(app,db)

# Let's create our first model!
# We inherit from db.Model class
class Puppy(db.Model):

    # If you don't provide this, the default table name will be the class name
    __tablename__ = 'puppies'

    # Now create the columns
    # Lots of possible types. We'll introduce through out the course
    # Full docs: http://docs.sqlalchemy.org/en/latest/core/types.html

    ### -- CREATE THE COLUMNS FOR THE TABLE

    # The columns will be: id (primary key), name, age

    # Primary Key column, unique id for each puppy
    id = db.Column(db.Integer,primary_key=True)
    # Puppy name
    name = db.Column(db.Text)
    # Puppy age in years
    age = db.Column(db.Integer)
    # Puppy breed, added to test migrations
    breed = db.Column(db.Text)

    # This sets what an instance in this table will have, i.e., a ROW.
    # Note the id will be auto-created for us later, so we don't add it here!
    def __init__(self,name,age,breed='Unknown'):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        # This is the string representation of a puppy in the model
        # I.e., when we want to print a ROW.
        return f"Puppy {self.name} is {self.age} years old."
