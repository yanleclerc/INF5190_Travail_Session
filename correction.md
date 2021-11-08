# Correction

## Tâches accomplies

- A1 - `manage.py`
- A2 - `app.py`
- A3 - `bgscheduler.py`
- A4 - `/doc`
- A5 - Je n'ai pas réussi à afficher le tableau dynamiquement.
  Par contre, l'appel Ajax ainsi que les fonctionnalités sont complétées.
  
- B1 - Il suffit de changer le courriel du fichier `courriels.yaml`
- B2 - voir `https://twitter.com/LInf5190`
- C1 - `/doc`
- C2 - `/doc`
- C3 - `/doc`
- D1 - `/doc` et `/api/requete`
- D2 - /doc.
- E1 - /doc.

## Faire fonctionner le programme

### Script de base

- Pour initialiser la base de données.

```
$ python3
>>> from app import db
>>> db.create_all()
>>> exit()
```

- Ensuite pour vérifier que la création a bien fonctionner :

```
sqlite3 database.db
sqlite> .tables
// declarations devrait être affiché
sqlite> .exit
```

### Librairies importées

- SQLAlchemy
- JsonSchema
- csv
- PyYAML
- TwitterAPI
- dicttoxml
- flask_json_schema
```
pip3 install flask_json_schema
```
- pycodestyle
```
pip3 install pycodestyle
```
- raml2html
```
  npm i -g raml2html  
```
- underscore.js
```
  npm install underscore
```
Sinon voir dans defaut.html, dernière balise "script"

