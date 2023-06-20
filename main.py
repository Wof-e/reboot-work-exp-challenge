from flask import (Flask,
                   render_template,
                   request,
                   send_from_directory)

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

from pathlib import Path
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "consumerlending"


class PackageForm(FlaskForm):
    submit = SubmitField("package_form")


@app.route('/', methods=['GET', 'POST'])
def student_or_employee():
    form = PackageForm()

    if request.form.get("action") == "Student":
        return render_template("welcome_to_experiences.html", form2=form)
    if request.form.get("action") == "Employee":
        return render_template("employee_form.html", form2=form)
    return render_template("home.html", form2=form)


if __name__=="__main__":
    app.run(debug=True)