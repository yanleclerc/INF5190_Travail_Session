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
import os
# pip3 import requests
import requests
import csv
from app import db, Declarations


def import_data():
    req = requests.get(
        "https://data.montreal.ca/dataset/49ff9fe4-eb30-4c1a-a30a-fca82d4f5c2f/resource/6173de60-c2da-4d63-bc75-0607cb8dcb74/download/declarations-exterminations-punaises-de-lit.csv")
    url_content = req.content
    csv_file = open('declarations-exterminations-punaises-de-lit.csv', 'wb')

    csv_file.write(url_content)
    csv_file.close()


def data_handler():
    # Pour que ça soit telechargé chaque jour a minuit dans le backgroundshceduler
    import_data()

    with open('declarations-exterminations-punaises-de-lit.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            # recuperation des variables
            # TODO : conversion en format convivial pour la bd
            num_declaration = row[0]
            date_declaration = row[1]
            date_insp_vispre = row[2]
            nbr_extermin = row[3]
            date_debuttrait = row[4]
            date_fintrait = row[5]
            n_qr = row[6]
            nom_qr = row[7]
            nom_arrond = row[8]
            coord_x = row[9]
            coord_y = row[10]
            longitude = row[11]
            latitude = row[12]

            # Pour éviter les duplications
            check_db = db.session.query(Declarations).filter_by(num_declaration=num_declaration,
                                                                date_declaration=date_declaration,
                                                                date_insp_vispre=date_insp_vispre,
                                                                nbr_extermin=nbr_extermin,
                                                                date_debuttrait=date_debuttrait,
                                                                date_fintrait=date_fintrait, n_qr=n_qr, nom_qr=nom_qr,
                                                                nom_arrond=nom_arrond, coord_x=coord_x, coord_y=coord_y,
                                                                longitude=longitude, latitude=latitude).all()
            if len(check_db) == 0:
                declaration = Declarations(num_declaration=num_declaration, date_declaration=date_declaration,
                                           date_insp_vispre=date_insp_vispre, nbr_extermin=nbr_extermin,
                                           date_debuttrait=date_debuttrait, date_fintrait=date_fintrait, n_qr=n_qr,
                                           nom_qr=nom_qr, nom_arrond=nom_arrond, coord_x=coord_x, coord_y=coord_y,
                                           longitude=longitude, latitude=latitude)
                db.session.add(declaration)
                db.session.commit()
            else:
                print('existe')
                pass
    csvfile.close()


if __name__ == '__main__':
    data_handler()
