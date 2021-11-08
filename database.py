import sqlite3
from declaration import Declaration
from utilisateur import Utilisateur
from requete import Requete


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

    # noinspection SqlInsertValues
    def create_declaration(self, num_declaration, date_declaration,
                           date_insp_vispre, nbr_extermin, date_debuttrait,
                           date_fintrait, n_qr, nom_qr, nom_arrond, coord_x,
                           coord_y, longitude, latitude):
        connection = self.get_connection()
        connection.execute((
            "insert into declarations("
            "num_declaration, date_declaration, date_insp_vispre,"
            " nbr_extermin, date_debuttrait, date_fintrait, n_qr,"
            " nom_qr, nom_arrond, coord_x,"
            " coord_y, longitude, latitude)"
            " values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"),
            (
                num_declaration, date_declaration, date_insp_vispre,
                nbr_extermin, date_debuttrait,
                date_fintrait, n_qr, nom_qr, nom_arrond, coord_x,
                coord_y, longitude, latitude))
        connection.commit()

    def get_declarations_recherche(self, nom_recherche):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from declarations where"
                       " nom_qr like ? OR nom_arrond like ? "
                       "ORDER BY num_declaration",
                       (nom_recherche, nom_recherche,))

        declarations_recherche = cursor.fetchall()
        if len(declarations_recherche) == 0:
            return None
        else:
            return (Declaration(declaration[0], declaration[1], declaration[2],
                                declaration[3],
                                declaration[4], declaration[5], declaration[6],
                                declaration[7],
                                declaration[8], declaration[9],
                                declaration[10], declaration[11],
                                declaration[12], declaration[13]) for
                    declaration in declarations_recherche)

    def get_declarations_dates(self, date_debuttrait, date_fintrait):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from declarations where"
                       " date_debuttrait >= ? "
                       "AND date_fintrait <= ? "
                       "ORDER BY num_declaration",
                       (date_debuttrait, date_fintrait,))

        declarations_dates = cursor.fetchall()

        if len(declarations_dates) == 0:
            return None
        else:
            return (Declaration(declaration[0], declaration[1], declaration[2],
                                declaration[3],
                                declaration[4], declaration[5], declaration[6],
                                declaration[7],
                                declaration[8], declaration[9],
                                declaration[10], declaration[11],
                                declaration[12], declaration[13]) for
                    declaration in declarations_dates)

    def get_liste_quartiers(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select nom_qr, COUNT(nom_qr) as compteur "
                       "from declarations where"
                       " nom_qr is not null "
                       "GROUP BY nom_qr having compteur > 1 "
                       "ORDER BY compteur DESC;",
                       )
        liste_quartier = cursor.fetchall()
        if len(liste_quartier) == 0:
            return None
        else:
            return [{"nom_qr": quartier[0], "compteur": quartier[1]} for
                    quartier in liste_quartier]

    def create_user(self, nom, courriel, liste_qr, password):
        connection = self.get_connection()
        connection.execute((
            "insert into utilisateurs("
            "nom, courriel, liste_qr,"
            " password) "
            "values(?, ?, ?, ?)"),
            (
                nom, courriel, liste_qr, password,))

        connection.commit()

        cursor = connection.cursor()
        cursor.execute("select * from utilisateurs"
                       " where Id=(SELECT last_insert_rowid())")
        result = cursor.fetchall()

        return result

    def create_requete(self, nom_qr, nom_arrond, adresse, date_visite,
                       nom_complet, description):
        connection = self.get_connection()
        connection.execute((
            "insert into requetes("
            " nom_qr, nom_arrond, adresse,"
            " date_visite, nom_complet, description) "
            "values(?, ?, ?, ?, ?, ?)"),
            (
                nom_qr, nom_arrond, adresse, date_visite, nom_complet,
            description,))

        connection.commit()

        cursor = connection.cursor()
        cursor.execute("select * from requetes"
                       " where Id=(SELECT last_insert_rowid())")
        result = cursor.fetchall()

        return result

    def get_requete(self, requete_id):
        cursor = self.get_connection().cursor()
        cursor.execute("select id, nom_qr, nom_arrond, adresse, date_visite,"
                       " nom_complet, description from requetes where"
                       " id = ?", (requete_id,))
        requetes = cursor.fetchall()
        if len(requetes) == 0:
            return None
        else:
            requete = requetes[0]
            return Requete(requete[0], requete[1], requete[2], requete[3],
                           requete[4], requete[5], requete[6])

    def delete_requete(self, requete):
        connection = self.get_connection()
        connection.execute("delete from requetes where rowid = ?",
                           (requete.id,))
        connection.commit()
