class Utilisateur:
    def __init__(self, id, nom, courriel, liste_qr, password):
        self.id = id
        self.nom = nom
        self.courriel = courriel
        self.liste_qr = liste_qr
        self.password = password

    def as_dictionary(self):
        return {"id": self.id,
                "nom": self.nom,
                "courriel": self.courriel,
                "liste_qr": self.liste_qr,
                "password": self.password}
