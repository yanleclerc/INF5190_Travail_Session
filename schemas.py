utilisateur_insert_schema = {
    'type': 'object',
    'required': ['nom', 'courriel',
                 'liste_qr', 'password'],
    'properties': {
        'nom': {
            'type': 'string'
        },
        'courriel': {
            'type': 'string'
        },
        'liste_qr': {
            'type': 'string'
        },
        'password': {
            'type': 'string'
        }
    },
    'additionalProperties': False
}

requetes_insert_schema = {
    'type': 'object',
    'required': ['nom_qr', 'nom_arrond',
                 'adresse', 'date_visite', 'nom_complet', 'description'],
    'properties': {
        'nom_qr': {
            'type': 'string'
        },
        'nom_arrond': {
            'type': 'string'
        },
        'adresse': {
            'type': 'string'
        },
        'date_visite': {
            'type': 'string'
        },
        'nom_complet': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        }
    },
    'additionalProperties': False
}
