"""
 Copyright 2021 Ela El-Heni
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from datetime import datetime
from flask import Flask
from flask import g
from flask import redirect
from flask import render_template, jsonify
from flask import request
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from dicttoxml import dicttoxml
from database import Database
from schemas import utilisateur_insert_schema
from schemas import requetes_insert_schema
from flask_json_schema import JsonSchema
from flask_json_schema import JsonValidationError
import pandas


app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
db = SQLAlchemy(app)
schema = JsonSchema(app)


class Declarations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_declaration = db.Column(db.BigInteger, nullable=False)
    date_declaration = db.Column(db.String(120), nullable=False,
                                 default=datetime.utcnow)
    date_insp_vispre = db.Column(db.String(120), nullable=False)
    nbr_extermin = db.Column(db.Integer, nullable=True)
    date_debuttrait = db.Column(db.String(120), nullable=True)
    date_fintrait = db.Column(db.String(120), nullable=True)
    n_qr = db.Column(db.String(20), nullable=False)
    nom_qr = db.Column(db.String(60), nullable=False)
    nom_arrond = db.Column(db.String(120), nullable=False)
    coord_x = db.Column(db.String(20), nullable=False)
    coord_y = db.Column(db.String(20), nullable=False)
    longitude = db.Column(db.String(20), nullable=False)
    latitude = db.Column(db.String(20), nullable=False)


class Utilisateurs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), nullable=False)
    courriel = db.Column(db.String(120), nullable=False)
    liste_qr = db.Column(db.String(500), nullable=False)
    password = db.Column(db.String(120), nullable=False)


class Requetes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_qr = db.Column(db.String(120), nullable=False)
    nom_arrond = db.Column(db.String(120), nullable=False)
    adresse = db.Column(db.String(500), nullable=False)
    date_visite = db.Column(db.String(120), nullable=False)
    nom_complet = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=False)


# Raccourci connection pour la base de données. Copyright de Jacques Berger :
# https://github.com/jacquesberger/exemplesINF5190
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(JsonValidationError)
def validation_error(e):
    errors = [validation_error.message for validation_error in e.errors]
    return jsonify({'error': e.message, 'errors': errors}), 400


@app.route('/', methods=["GET", "POST"])
def generer_tableau_accueil():
    if request.method == "GET":
        return render_template("accueil.html")
    else:
        nom_recherche = request.form["nom_QA"]
        if nom_recherche == "":
            error = "Veuillez remplir les cases vides/respecter les" \
                    " instructions."
            return render_template("accueil.html", error=error)
        else:
            return redirect(url_for('generer_tableau_recherche',
                                    nom_recherche=nom_recherche))


@app.route('/recherche/<nom_recherche>')
def generer_tableau_recherche(nom_recherche):
    nom = '%' + nom_recherche + '%'
    db = get_db()
    taches = db.get_declarations_recherche(nom)
    return render_template("recherches.html", taches=taches)


@app.route('/doc')
def afficher_documentation():
    return render_template("doc.html")


@app.route('/api/declaration/du=<date_debuttrait>&au=<date_fintrait>')
def get_declarations_dates(date_debuttrait, date_fintrait):
    db = get_db()
    declarations = db.get_declarations_dates(date_debuttrait, date_fintrait)
    if declarations is None:
        return "", 404
    else:
        return jsonify([declaration.as_dictionary() for declaration
                        in declarations])


@app.route('/api/quartiers/json')
def get_liste_quartiers_json():
    db = get_db()
    liste_quartier = db.get_liste_quartiers()
    if liste_quartier is None:
        return "", 404
    else:
        return jsonify(liste_quartier)


@app.route('/api/quartiers/xml')
def get_liste_quartiers_xml():
    db = get_db()
    liste_quartier = db.get_liste_quartiers()
    if liste_quartier is None:
        return "", 404
    else:
        return dicttoxml(liste_quartier, custom_root='Zonelist',
                         attr_type=False)


@app.route('/api/quartiers/csv')
def get_liste_quartiers_csv():
    db = get_db()
    liste_quartier = db.get_liste_quartiers()
    if liste_quartier is None:
        return "", 404
    else:
        df = pandas.DataFrame.from_dict(liste_quartier)
        return df.to_csv()


@app.route('/api/inscription', methods=['POST'])
@schema.validate(utilisateur_insert_schema)
def post_inscription():
    data = request.get_json()
    utilisateur = get_db().create_user(data["nom"], data["courriel"],
                                       data["liste_qr"],
                                       data["password"])
    return jsonify(utilisateur), 201


@app.route('/api/requete', methods=['GET', 'POST'])
@schema.validate(requetes_insert_schema)
def post_requete():
    if request.method == "GET":
        return render_template('requete.html')
    else:
        data = request.get_json()
        utilisateur = get_db().create_requete(data["nom_qr"],
                                              data["nom_arrond"],
                                              data["adresse"],
                                              data["date_visite"],
                                              data["nom_complet"],
                                              data["description"])
    return jsonify(utilisateur), 201


@app.route('/api/requete/<id>', methods=["DELETE"])
def delete_person(id):
    requete = get_db().get_requete(id)
    if requete is None:
        return "", 404
    else:
        get_db().delete_requete(requete)
        return "", 200
