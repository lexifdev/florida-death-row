from flask import Flask, render_template, redirect, url_for
from roster import ROSTER

app = Flask(__name__)
#app.config['SECRET_KEY'] = '14uff!eumps&w00ze!s'
application = app


# get the information for each ID
def get_inmatedata(source, id):
    return next((data for data in ROSTER if data['id'] == id))


# set the homepage and the /restaurants.html to run the function to get information using the python dictionary INSPECTIONS
@app.route('/')
@app.route('/inmates.html')
def inmates():
    return render_template('inmates.html', roster=ROSTER)


# make a path for the /restaurant with each restaurant id and show the information for each restaurant with each ID
@app.route('/inmate/<id>.html')
def inmate(id):
    inmatedata = get_inmatedata(ROSTER, id)
    return render_template('inmate.html', inmate=inmatedata)


if __name__ == '__main__':
    app.run(debug=True)
