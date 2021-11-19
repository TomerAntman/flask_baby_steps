import sys
from flask import Flask, request, render_template, jsonify
from json import dumps
from markupsafe import escape

app = Flask(__name__, template_folder='./templates')
sys.path.insert(1, '../wis-advanced-python-2021-2022/application')
import call_students2
list_of_keys = call_students2.get_key_list()
@app.route("/")
def main():
    return render_template("main.html", title="Students", list_of_keys = list_of_keys)

# list all people
## see https://camposha.info/python-examples/flask-list-to-jinja2/
@app.route("/all_students")
def all():
    student_list = call_students2.call_students()
    return render_template("student_list.html", the_list = student_list)

# Link to details after clicking:
@app.route('/all_students/<student_name>', methods=['GET', 'POST'])
def profile(student_name):
    # app.jinja_env.filters['tojson_pretty'] = name_to_pretty_json(student_name)
    json_to_show = call_students2.name_to_json(student_name)
    return render_template('profile.html', student = json_to_show)

@app.route('/names_queried/', methods=['POST',"GET"])
def query():
    list_of_keys = call_students2.get_key_list()
    dictionary1={}
    for key in list_of_keys:
        some_value = str(request.args.get(f'{key}'))
        # everything is entered as a list
        if some_value != "":
            dictionary1[key] = some_value.split(", ")
    # return dictionary1
    searched_students = call_students2.search_engine(dictionary1)
    # return (jsonify(searched_students))
    return render_template("student_list.html", the_list = searched_students)



app.run(debug=True)