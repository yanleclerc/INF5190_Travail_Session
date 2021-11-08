function validerNomQA() {
    let nom = document.getElementById("nom_QA").value;

    if (nom === '') {
        document.getElementById("invalid_nom_QA").innerHTML =
            "Le champ est vide, Veuillez saisir un nom.";
        return false
    }
}

function validerDates() {
    let dateD = document.getElementById("date_debut").value;
    let dateF = document.getElementById("date_fin").value;
    let formatDate = new RegExp(/\d{4}-\d{2}-\d{2}/i);


    if (!formatDate.test(dateD)) {
        document.getElementById("invalid_date_debut").innerHTML =
            "Le format de date fin est invalide. (ISO 8601)";
        return false

    } else if (!formatDate.test(dateF)) {
        document.getElementById("invalid_date_fin").innerHTML =
            "Le format de date fin est invalide. (ISO 8601)";
        return false

    } else if (parseInt(dateD.split('-')) > parseInt(dateF.split('-'))) {
        document.getElementById("invalid_date_debut").innerHTML =
            "La date début est invalide.";
        return false
    }
    get_declarations(dateD, dateF)
}

function get_declarations(date_debuttrait, date_fintrait) {
    fetch('/api/declaration/du=' + date_debuttrait + '&au=' + date_fintrait)
        .then(function (response) {
            return response.json();
        }).then(function (json) {
        let reponse = _.groupBy(json,'nom_qr');
        console.log('FETCH response:');
        console.log(reponse);

        //Afficher tableau

    });
}

function validerRequete(){

    let nom_qr = document.getElementById('inputNomQr').value;
    let nom_arrond = document.getElementById('inputNomArrond').value;
    let adresse = document.getElementById('inputAdresse').value;
    let date_visite = document.getElementById('inputDateVisite').value;
    let nom_complet = document.getElementById('inputNomResident').value;
    let description = document.getElementById('inputDescription').value;

    if(nom_qr.length >= 5 || nom_qr.length > 120){
        document.getElementById('').innerHTML =
            'Le champ est vide/invalide ou dépasse la limite de 120 charactères.'
        return false
    } else if(nom_arrond.length >= 5 || nom_arrond.length > 120){
        document.getElementById('').innerHTML =
            'Le champ est vide/invalide ou dépasse la limite de 120 charactères.'
        return false
    } else if(adresse.length >= 5 || adresse.length > 500){
        document.getElementById('').innerHTML =
            'Le champ est vide/invalide ou dépasse la limite de 500 charactères.'
        return false
    }else if (!validerFormatDate(date_visite)) {
        document.getElementById('').innerHTML =
            'La date ne respecte pas le format JJ-MM-AAAA ou est invalide.'
        return false
    } else if(nom_complet.length >= 5 || nom_complet.length > 120){
        document.getElementById('').innerHTML =
            'Le champ est vide/invalide ou dépasse la limite de 120 charactères.'
        return false
    } else if(description.length >= 5 || description.length > 500){
        document.getElementById('').innerHTML =
            'Le champ est vide ou dépasse la limite de 500 charactères.'
        return false
    }

    envoyer_requete()

}

function validerFormatDate(date){
    let formatDate = new RegExp(/\d{4}-\d{2}-\d{2}/i);

    if (!formatDate.test(date)) {
        return false
    } else if (!validerDateFutur(date)){
        return false
    }
}

function validerDateFutur(date){
    let test = date.split('-');
    let limite = new Date().toISOString().slice(0, 10).split('-');

    return test >= limite;
}

function envoyer_requete(){
    fetch('/api/requete', {
    method: 'POST',
    body: document.getElementById('formElem'), // string or object
    headers: {
      'Content-Type': 'application/json'
    }
  });
}