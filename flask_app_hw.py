import sys
from flask import Flask, request, render_template, jsonify
from json import dumps
from markupsafe import escape

app = Flask(__name__, template_folder='./templates')

@app.route("/")
def main():
    return render_template("main.html", title="Students")

# list all people
## see https://camposha.info/python-examples/flask-list-to-jinja2/
@app.route("/all_students")
def all():
    sys.path.insert(1, '../wis-advanced-python-2021-2022/application')
    from call_students import call_students
    student_list = call_students()
    return render_template("student_list.html", the_list = student_list)

# Link to details after clicking:
@app.route('/all_students/<student_name>', methods=['GET', 'POST'])
def profile(student_name):
    sys.path.insert(1, '../wis-advanced-python-2021-2022/application')
    from call_students import name_to_pretty_json

    # app.jinja_env.filters['tojson_pretty'] = name_to_pretty_json(student_name)
    json_to_show = name_to_pretty_json(student_name)
    return render_template('profile.html', student = json_to_show)

app.run(debug=True)