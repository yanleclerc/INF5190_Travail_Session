class Requete:
    def __init__(self, id, nom_qr, nom_arrond, adresse, date_visite,
                 nom_complet, description):
        self.id = id
        self.nom_qr = nom_qr
        self.nom_arrond = nom_arrond
        self.adresse = adresse
        self.date_visite = date_visite
        self.nom_complet = nom_complet
        self.description = description

    def as_dictionary(self):
        return {"id": self.id,
                "nom_qr": self.nom_qr,
                "nom_arrond": self.nom_arrond,
                "adresse": self.adresse,
                "date_visite": self.date_visite,
                "nom_complet": self.nom_complet,
                "description": self.description}
