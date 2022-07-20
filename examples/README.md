# Examples of Flask Applications

Many examples collected in this repository come from:

- The Udemy course by José Marcial Portilla [Python and Flask Bootcamp: Create Websites using Flask](https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask).

## Usage

First, install Flask on your preferred environment:

```bash
# Select environment
conda activate ds
# Install if not done yet
conda install -c anaconda flask  -y
conda install -c anaconda flask-wtf  -y
```

Then select the script/application you would like to run:

```bash
python hello_world.py
```

For a detailed guide on how to use Flask and the content of the examples: `../flask_guide.md`.

## Example Files

Each section in the guide has its own sub-folder with examples.

- `01_basics/`
	- [`hello_world`](./01_basics/hello_world.py)
	- [`dynamic_routes.py`](./01_basics/dynamic_routes.py)
- `02_templates`