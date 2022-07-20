# Run: python basic_template.py

# Import the render_template function
from flask import Flask, render_template
app = Flask(__name__)

# Render an HTML template file
# All templates are located in the folder templates (Flask looks for that name)
# This template uses an image in the folder static
# The folder name with the resources is arbitrary
@app.route('/')
def index():
    # Connecting to a template (html file)
    return render_template('basic-template.html')

# Debug mode active; deactivate to go to production
if __name__ == '__main__':
    app.run(debug=True)
