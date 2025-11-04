function habilitarNotas(materia) {
  var fila = document.getElementById(materia);
  var notas = fila.querySelectorAll(".nota");
  var checkbox = fila.querySelector('input[type="checkbox"]');
  var botonPromedio = fila.querySelector("input[type='button']");
  var mensajePromedio = fila.querySelector(".mensajePromedio");

  if (checkbox.checked) {
    notas.forEach((nota) => {
      nota.disabled = false;
    });

    botonPromedio.disabled = false;
    mensajePromedio.disabled = false;
  } else {
    notas.forEach((nota) => (nota.disabled = true));

    botonPromedio.disabled = true;
    mensajePromedio.disabled = true;
  }
}

function verPromedio(materia) {
  var fila = document.getElementById(materia);
  var listaNotas = fila.querySelectorAll(".nota");

  var sumaNotas = 0;
  var totalNotas = 0;
  console.log(listaNotas);

  listaNotas.forEach((nota) => {
    sumaNotas += parseInt(nota.value);
    totalNotas++;
  });

  promedio = (sumaNotas / totalNotas).toFixed(2);

  fila.querySelector(".mensajePromedio").value = promedio;
}

function validarDatos() {
  if (
    document.getElementById("nombre").value.length == 0 ||
    document.getElementById("apellido").value.length == 0 ||
    document.getElementById("dni").value.length == 0 ||
    document.getElementById("domicilio").value.length == 0 ||
    document.getElementById("nacimiento").value.length == 0
  ) {
    alert("Falta completar información en Datos personales");
  } else if ( document.querySelectorAll('input[type="checkbox"]:checked').length < 5){
    alert("Debe haber seleccionado un minimo de 5 materias")
  }

  else{
    let info = document.querySelectorAll('input[type="checkbox"]:checked')
    alert("TODOS LOS DATOS ESTAN CORRECTOS")
    console.log(
      info
    );
    
  }
}
