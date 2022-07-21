# This is a very simple script that will show you how to setup our DB
# Later on we'll want to use this type of code with templates

### NOTE!! If you run this script multiple times you will add
### multiple puppies to the database. That is okay, just the
### ids will be higher than 1, 2 on the subsequent runs

# Import database info
from basic_model_app import db, Puppy

# Create the tables in the database
# db was instantiated in basic_model_app
# The SQLite database file appears in its path 
# (Usually won't do it this way!)
db.create_all()

# Create new entries in the database
sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

# Check ids
# We haven't added sam and frank to database, so they should be None.
# Note that id is the primary key, set when creating a columns
print(sam.id)
print(frank.id)

# Ids will get created automatically once we add these entries to the DB
# Note we use session: db.session
db.session.add_all([sam,frank])

# Alternative for individual additions:
# db.session.add(sam)
# db.session.add(frank)

# Now save it to the database
db.session.commit()

# Check the ids
# Now we get the ids
print(sam.id)
print(frank.id)
