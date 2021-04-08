# Correction

## Tâches accomplies

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
