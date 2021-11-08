run :
	export FLASK_APP=app.py
	export FLASK_ENV=development
	flask run

raml2html :
	raml2html doc.raml > templates/doc.html
	flask run