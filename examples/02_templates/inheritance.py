# Run: python inheritance.py

from flask import Flask, render_template
app = Flask(__name__)

# Home page
# The HTML file inherits from inheritance-base.html
# which contains a common Bootstrap nav-bar
@app.route('/')
def index():
    return render_template('inheritance-home.html')

# Puppy name page
# The HTML file inherits from inheritance-base.html
# which contains a common Bootstrap nav-bar
@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('inheritance-puppy.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)
