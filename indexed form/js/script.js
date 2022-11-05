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
        //Datos Personales
        document.getElementById('nombre').value             = user.nombre;
        document.getElementById('inicial').value            = user.inicial;
        document.getElementById('apellidos').value          = user.apellidos;
        document.getElementById('seguroSocial').value       = user.seguroSocial;
        document.getElementById('email').value              = user.email;
        document.getElementById('phone').value              = user.phone;
        
        // Direccion Fisica
        document.getElementById('direccionFisica1').value   = user.direccionFisica1;
        document.getElementById('direccionFisica2').value   = user.direccionFisica2;
        document.getElementById('ciudadFisica').value       = user.ciudadFisica;
        document.getElementById('estadoFisico').value       = user.estadoFisico;
        document.getElementById('zipcodeFisico').value      = user.zipcodeFisico;

        if (user.fisicaCorreo > 0) {
          $('#direccionCorreo').addClass("d-none");
        }
        else {
          document.getElementById('fisicaCorreo').checked = false;
          $('#direccionCorreo').removeClass("d-none");
        }

        $('#fisicaCorreo').change(function () {
          if ($(this).is(":checked")) {
            $('#direccionCorreo').addClass("d-none");
            $('#direccionCorreo1').attr('required', false);
            $('#ciudadCorreo').attr('required', false);
            $('#estadoCorreo').attr('required', false);
            $('#zipCorreo').attr('required', false);                
          } else {
            $('#direccionCorreo').removeClass("d-none");
            $('#direccionCorreo1').attr('required', true);
            $('#ciudadCorreo').attr('required', true);
            $('#estadoCorreo').attr('required', true);
            $('#zipCorreo').attr('required', true);
            $('#direccionCorreo1').val() = $('#direccionFisica1').val();

            //Direccion de Correo
            document.getElementById('direccionCorreo1').value = user.direccionCorreo1;
            document.getElementById('direccionCorreo2').value = user.direccionCorreo2;
            document.getElementById('estadoCorreo').value     = user.estadoCorreo;
            document.getElementById('zipcodeCorreo').value    = user.zipcodeCorreo;
          }
        });
                        
        //Informacion de Contacto
        document.getElementById('contactoEmergencia').value = user.contactoEmergencia;
        document.getElementById('parentesco').value         = user.parentesco;
        document.getElementById('telefonoContacto').value   = user.telefonoContacto;

        //Elegibilidad
        if (user.elegibilidad == "Sí") {$('#elegibilidad1').attr('checked', true);}
        else { $('#elegibilidad2').attr('checked', true)}

        //Turno
        if (user.turno == "Sí") {$('#turno1').attr('checked', true);}
        else { $('#turno2').attr('checked', true)}

        //Experiencia Laboral
        document.getElementById('nombrePatrono').value    = user.nombrePatrono;
        document.getElementById('titulo').value           = user.titulo;
        document.getElementById('nombreSupervisor').value = user.nombreSupervisor;
        document.getElementById('telefonoPatrono').value  = user.telefonoPatrono;
        document.getElementById('periodo').value          = user.periodo;
        document.getElementById('razonTerminacion').value = user.razonTerminacion;

        //Prparacion Academica
        document.getElementById('school').value          = user.school;
        document.getElementById('periodoEstudios').value = user.periodoEstudios;
        document.getElementById('grado').value           = user.grado;
        if (user.graduado == "Sí") {$('#graduado1').attr('checked', true);}
        else { $('#graduado2').attr('checked', true)}
        
        //Background Check
        if (user.convicto == "Sí") {$('#convicto1').attr('checked', true);}
        else { $('#convicto2').attr('checked', true)}

        //Salario
        const salarioButtons = document.querySelectorAll('input[name="salario"]');
        for (const salary of salarioButtons) {
          if (salary.value == user.salario) {
            document.getElementById(salary.id).checked = true;
            break;
          }
        }

        // document.getElementById('xx').value = user.xx;

        console.table(user);
        console.log(user.nombre);        
      }
    } else { // key not exist
      // $('#direccionCorreo').addClass("d-none");
      $('#fisicaCorreo').change(function () {
        if ($(this).is(":checked")) {
          $('#direccionCorreo').addClass("d-none");
          $('#direccionCorreo1').attr('required', false);
          $('#ciudadCorreo').attr('required', false);
          $('#estadoCorreo').attr('required', false);
          $('#zipCorreo').attr('required', false);                
        } else {
          $('#direccionCorreo').removeClass("d-none");
          $('#direccionCorreo1').attr('required', true);
          $('#ciudadCorreo').attr('required', true);
          $('#estadoCorreo').attr('required', true);
          $('#zipCorreo').attr('required', true);
          $('#direccionCorreo1').val() = $('#direccionFisica1').val();
        }
      });
      console.log('Formulario vacio');
    }

    // Disponibilidad de turno
    $('#turno1').change(function () {
      if ($(this).is(":checked")) {
        $('#disponibilidad').addClass("d-none", 3000, "easeInBack");            
      }
    });
    $('#turno2').change(function () {
      if ($(this).is(":checked")) {
        $('#disponibilidad').removeClass("d-none", 3000, "easeInBack");               
      }
    });
    

    // Backgroung check
    $('#convicto1').change(function () {
      if ($(this).is(":checked")) {
        $('#detallesConvicto').removeClass("d-none");            
      }
    });
    $('#convicto2').change(function () {
      if ($(this).is(":checked")) {
        $('#detallesConvicto').addClass("d-none");            
      }
    });
  };

  form.addEventListener('submit', handleFormSubmit);

};


function handleFormSubmit(e) {
  e.preventDefault();

  const db       = request.result;
  const data     = new FormData(e.target);
  const formJSON = Object.fromEntries(data.entries());

  console.table(formJSON)

  insertCandidate(db, formJSON);



function insertCandidate(db, table) {

  const txn   = db.transaction(DB_STORE_NAME, 'readwrite');
  const store = txn.objectStore(DB_STORE_NAME);

  let query   = store.put(table);

  query.onsuccess = function (e) { 
    console.log(e);
    window.alert("Su data fue almacenada correctamente");
    document.getElementById("contact-form").reset();
  };

  query.onerror   = function (e) {
    console.log(e.target.errorCode)
  };

  txn.oncomplete  = function () {
    db.close()
  };
}
}
