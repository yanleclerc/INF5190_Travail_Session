import sqlite3


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/database.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def create_tache(self, NO_DECLARATION, DATE_DECLARATION, DATE_INSP_VISPRE, NBR_EXTERMIN, DATE_DEBUTTRAIT,
                     DATE_FINTRAIT, No_QR, NOM_QR, NOM_ARROND, COORD_X, COORD_Y, LONGITUDE, LATITUDE):
        connection = self.get_connection()
        connection.execute(("insert into Declarations(NO_DECLARATION, DATE_DECLARATION, DATE_INSP_VISPRE,"
                            " NBR_EXTERMIN, DATE_DEBUTTRAIT, DATE_FINTRAIT, No_QR, NOM_QR, NOM_ARROND, COORD_X,"
                            " COORD_Y, LONGITUDE, LATITUDE)"
                            " values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"),
                           (NO_DECLARATION, DATE_DECLARATION, DATE_INSP_VISPRE,
                            NBR_EXTERMIN, DATE_DEBUTTRAIT, DATE_FINTRAIT, No_QR, NOM_QR, NOM_ARROND, COORD_X,
                            COORD_Y, LONGITUDE, LATITUDE))
        connection.commit()

    def get_taches(self, nom_quartier, nom_arrondissement):
        cursor = self.get_connection().cursor()
        cursor.execute("select NO_DECLARATION, DATE_DECLARATION, DATE_INSP_VISPRE,"
                       " NBR_EXTERMIN, DATE_DEBUTTRAIT, DATE_FINTRAIT, No_QR, NOM_QR, NOM_ARROND, COORD_X,"
                       " COORD_Y, LONGITUDE, LATITUDE from exterminations where"
                       " NOM_QR = ? OR NOM_ARROND = ?  ORDER BY date(DATE_DECLARATION)", (nom_quartier,
                                                                                          nom_arrondissement,))
        taches = cursor.fetchall()
        return [{"NO_DECLARATION": tache[0], "DATE_DECLARATION": tache[1], "DATE_INSP_VISPRE": tache[2],
                 "NBR_EXTERMIN": tache[3], "DATE_DEBUTTRAIT": tache[4], "DATE_FINTRAIT": tache[5],
                 "No_QR": tache[6], "NOM_QR": tache[7], "NOM_ARROND": tache[8], "COORD_X": tache[9],
                 "COORD_Y": tache[10], "LONGITUDE": tache[11], "LATITUDE": tache[12]}
                for tache in taches]
