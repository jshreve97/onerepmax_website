from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'secret'


class OneRepMaxForm(FlaskForm):
    weight_lifted = IntegerField('Weight Lifted (in pounds)', validators=[DataRequired(), NumberRange(min=1)])
    reps_completed = IntegerField('Reps Completed', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Calculate')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = OneRepMaxForm()
    if form.validate_on_submit():
        weight_lifted = form.weight_lifted.data
        reps_completed = form.reps_completed.data
        one_rep_max = round(weight_lifted * (1 + reps_completed / 30), 2)
        return render_template('result.html', one_rep_max=one_rep_max)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
