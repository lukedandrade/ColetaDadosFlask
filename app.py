from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from configuration import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
btstrap = Bootstrap(app)

from datetime import datetime
from flask import render_template, flash, redirect, url_for, session
from models import Data
from forms import SelectAgeForm, FraseForm
from random import choice

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SelectAgeForm()

    if form.validate_on_submit():
        session['start_time'] = datetime.utcnow()
        frases = [
            'Eu sou inevitável',
            'Alan Turing, ateu homossexual, pai da ciência da computação',
            'Uma frase de exemplo',
            'Não, eu sou seu pai'
        ]
        session['secret_phrase'] = choice(frases)
        return redirect(url_for('coleta_dados', age_id=int(form.user_age.data)))

    return render_template('index.html',
                           title = 'Coleta de Dados para Rede Neural',
                           form=form)

@app.route('/coleta_dados/<int:age_id>', methods=['GET', 'POST'])
def coleta_dados(age_id):
    if age_id > 3 or age_id < 1:
        return redirect(url_for('index'))

    else:
        form = FraseForm()

        if form.validate_on_submit():
            if form.frase.data == session['secret_phrase']:
                finish = datetime.utcnow()
                new_data = Data(
                    char_num = len(session['secret_phrase']),
                    timedelta = (finish - session['start_time']).seconds,
                    age_id = age_id
                )
                db.session.add(new_data)
                db.session.commit()
                flash('Dados adicionados com sucesso, obrigado pela colaboração.')
                return redirect(url_for('index'))
            else:
                flash('As frases não estão iguais')
                return redirect(url_for('coleta_dados', age_id=age_id))
        else:
            return render_template('datainput.html',
                                   frase = session['secret_phrase'],
                                   form = form)

@app.route('/getresults')
def get_data():
    dados = Data.query.all()

    return render_template('dataretrieve.html',
                           title="Ó OS DADOS VINDO",
                           dados=dados)