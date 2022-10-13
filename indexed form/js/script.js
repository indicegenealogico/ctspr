const DB_NAME       = 'CTSPR',
      DB_VERSION    = 1,
      DB_STORE_NAME = 'Candidate';


// This works on all devices/browsers, and uses IndexedDBShim as a final fallback
const indexedDB =
  window.indexedDB ||
  window.mozIndexedDB ||
  window.webkitIndexedDB ||
  window.msIndexedDB ||
  window.shimIndexedDB;


if (!indexedDB) {
  window.alert("Your browser doesn't support a stable version of IndexedDB.")
}


// Open (or create) the database
const request = indexedDB.open(DB_NAME, DB_VERSION);


request.onerror = function (e) {
  console.error("An error occurred with IndexedDB:" + e.target.errorCode);
  console.error(e);
};


request.onupgradeneeded = function (e) {
  const db    = request.result;
  const table = db.createObjectStore(DB_STORE_NAME, {autoIncrement: true} );
};


request.onsuccess = function(e) {
  const db    = request.result;
  const txn   = db.transaction(DB_STORE_NAME, 'readwrite');
  const store = txn.objectStore(DB_STORE_NAME);
  const form  = document.querySelector('.contact-form');

  var req = store.openCursor();

  req.onsuccess = function(e) {
    var cursor = e.target.result; 
    if (cursor) { // key already exist Escribir codigo si el formulario fue llenado

      let data = store.get(1);
      
      data.onsuccess = function() {
        user = data.result;
        //Muestra el formulario lleno si existe data
        document.getElementById('nombre').value             = user.nombre;
        document.getElementById('inicial').value            = user.inicial;
        document.getElementById('apellidos').value          = user.apellidos;
        document.getElementById('seguroSocial').value       = user.seguroSocial;
        document.getElementById('email').value              = user.email;
        document.getElementById('direccionFisica1').value   = user.direccionFisica1;
        document.getElementById('direccionFisica2').value   = user.direccionFisica2;
        document.getElementById('ciudadFisica').value       = user.ciudadFisica;
        document.getElementById('estadoFisico').value       = user.estadoFisico;
        document.getElementById('zipcodeFisico').value      = user.zipcodeFisico;
        document.getElementById('fisicaCorreo').value       = user.fisicaCorreo;
        document.getElementById('direccionCorreo1').value   = user.direccionCorreo1;
        document.getElementById('direccionCorreo2').value   = user.direccionCorreo2;
        document.getElementById('estadoCorreo').value       = user.estadoCorreo;
        document.getElementById('zipcodeCorreo').value      = user.zipcodeCorreo;
        document.getElementById('contactoEmergencia').value = user.contactoEmergencia;
        document.getElementById('parentesco').value         = user.parentesco;
        //document.getElementById('xx').value = user.xx;
        //document.getElementById('xx').value = user.xx;


        
        console.table(user);
        console.log(user.nombre);
        
      }
    } else { // key not exist
      console.log('Formulario vacio');
    }
  };

  form.addEventListener('submit', handleFormSubmit);

};




function insertCandidate(db, table) {

  const txn   = db.transaction(DB_STORE_NAME, 'readwrite');
  const store = txn.objectStore(DB_STORE_NAME);

  let query   = store.put(table);

  query.onsuccess = function (e) { 
    console.log(e);
    window.alert("Su data fue almacenada correctamente");
    document.getElementById("contact-form").reset();
  };
  query.onerror   = function (e) { console.log(e.target.errorCode) };

  txn.oncomplete  = function () { db.close() };
}


function handleFormSubmit(e) {
  e.preventDefault();

  const db       = request.result;
  const data     = new FormData(e.target);
  const formJSON = Object.fromEntries(data.entries());

  console.table(formJSON)

  insertCandidate(db, formJSON);

  // for multi-selects, we need special handling
  //formJSON.snacks = data.getAll('snacks');
  
  // const results = document.querySelector('.results pre');
  // results.innerText = JSON.stringify(formJSON, null, 2);
}
