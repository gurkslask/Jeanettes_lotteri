from flask import Flask, render_template, jsonify, redirect, session
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import os


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object('config')

resultat_dict = {
        '41026180': 'Ingen vinst på denna lotten, men du har vunnit en lott till! Säg detta till närmaste man så fixar han det!',
        '61026042' : '''Du har vunnit ett presentkort på resor till ett värde av 3000kr ihop med din man
        detta kan användas till tex. en weekend i Göteborg, en spadag eller något annat roligt :)'''
        }

resultatet = 'Default'


class AForm(Form):
    Lottnummer = StringField('Lottnummer', validators=[Required()])

@app.route('/', methods=['GET', 'POST'])
def main2():
    form = AForm()
    if form.validate_on_submit():
        session['lottery'] = form.Lottnummer.data
        return redirect('/results')
    return render_template(
        'main.html',
        form=form,
        dLottnummer='Lottnummer',
    )


@app.route('/results', methods=['GET', 'POST'])
def results():
    try: 
        results = resultat_dict[session['lottery']]
    except KeyError:
        results = 'Tyvärr, lottnummret du har angett finns inte, försök igen!'

    return render_template(
            'results.html',
            results = results
            )
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
    # app.run(host='0.0.0.0')
