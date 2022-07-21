# Now that the table has been created by running: set_up_database.py
# basic_model_app and set_up_database we can play around with CRUD commands
# This is just an overview, usually we won't run a single script like this
# Our goal here is to just familiarize ourselves with CRUD commands

from basic_model_app import db, Puppy

### -- CREATE

my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

### -- READ

# Note lots of ORM filter options here.
# Basically, SQL statements are translated into python calls:
# filter(), filter_by(), limit(), order_by(), group_by()
# Also lots of executor options:
# all(), first(), get(), count(), paginate()

all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies) # [Puppy Sammy is 3 years old., Puppy Frankie is 4 years old., Puppy Rufus is 5 years old.]
print('\n')
# Grab by id
puppy_one = Puppy.query.get(1)
print(puppy_one) # Puppy Sammy is 3 years old.
print(puppy_one.age) # 3
print('\n')
# Filters, e.g., by column values (column name)
puppy_sam = Puppy.query.filter_by(name='Sammy') # Returns list
print(puppy_sam) # Sammy is 3 years old.
print('\n')

### -- UPDATE 

# Grab your data, then modify it, then save the changes.
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

### -- DELETE

second_pup = Puppy.query.get(2)
db.session.delete(second_pup) # error if second_pup doesn't exist
db.session.commit()

# Check for changes:
all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies) # [Puppy Sammy is 10 years old., Puppy Rufus is 5 years old.]
