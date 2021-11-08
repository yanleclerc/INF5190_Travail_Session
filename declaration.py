class Declaration:
    def __init__(self, id, num_declaration, date_declaration, date_insp_vispre,
                 nbr_extermin, date_debuttrait,
                 date_fintrait, n_qr, nom_qr, nom_arrond, coord_x, coord_y,
                 longitude, latitude):
        self.id = id
        self.num_declaration = num_declaration
        self.date_declaration = date_declaration
        self.date_insp_vispre = date_insp_vispre
        self.nbr_extermin = nbr_extermin
        self.date_debuttrait = date_debuttrait
        self.date_fintrait = date_fintrait
        self.n_qr = n_qr
        self.nom_qr = nom_qr
        self.nom_arrond = nom_arrond
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.longitude = longitude
        self.latitude = latitude

    def as_dictionary(self):
        return {"id": self.id,
                "num_declaration": self.num_declaration,
                "date_declaration": self.date_declaration,
                "date_insp_vispre": self.date_insp_vispre,
                "nbr_extermin": self.nbr_extermin,
                "date_debuttrait": self.date_debuttrait,
                "date_fintrait": self.date_fintrait,
                "n_qr": self.n_qr,
                "nom_qr": self.nom_qr,
                "nom_arrond": self.nom_arrond,
                "coord_x": self.coord_x,
                "coord_y": self.coord_y,
                "longitude": self.longitude,
                "latitude": self.latitude}
