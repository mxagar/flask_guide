# Examples of Flask Applications

Many examples collected in this repository come from the Udemy course by José Marcial Portilla [Python and Flask Bootcamp: Create Websites using Flask](https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask).

## Usage

First, install Flask on your preferred environment:

```bash
# Select environment
conda create --name ds pip
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

:construction:

Each section in the guide has its own sub-folder with examples. Additionally, each python script can use HTML templates located in the sub-folder `templates/` or assets/images located in `static/`.

- `01_basics/`
	- [`hello_world.py`](./01_basics/hello_world.py)
	- [`dynamic_routes.py`](./01_basics/dynamic_routes.py)
- `02_templates/`
	- [`basic_template.py`](./02_templates/basic_template.py)
	- [`variables.py`](./02_templates/variables.py)	
	- [`control_flow.py`](./02_templates/control_flow.py)
	- [`inheritance.py`](./02_templates/inheritance.py)
	- [`form.py`](./02_templates/form.py)
