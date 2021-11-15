import sys
from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html", title="Students")

# list all people
@app.route("/all_students")
def all():
    sys.path.insert(0, 'https://github.com/TomerAntman/wis-advanced-python-2021-2022/application')
    import call_students
    return (call_students.sorted_list)