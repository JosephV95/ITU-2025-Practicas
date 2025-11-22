function validarCampos() {
  var nombre = document.getElementById("nombre").value;
  var apellido = document.getElementById("apellido").value;
  var dni = document.getElementById("dni").value;
  if (nombre == "" || apellido == "" || dni == "") {
    alert("Complete todos los campos obligatorios.");
    return false;
  }
}

function verificarValores() {
    // validarCampos()
    
    var colesterol = document.getElementById("colesterol").value;
    var globulosRojos = document.getElementById("globulos_rojos").value;
    var globulosBlancos = document.getElementById("globulos_blancos").value;
    var glucemia = document.getElementById("glucemia").value;
    var trigliceridos = document.getElementById("trigliceridos").value;

    var datosGlobulos = {
        "rojos": globulosRojos,
        "blancos": globulosBlancos,
    }

    if (colesterol > 50 ) {

        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/globulos",
            data: JSON.stringify(datosGlobulos),
            headers: {
                "accept": "application/json",
                'Content-Type': 'application/json'
            },
            success: function (respuesta) {
                console.log(respuesta);
                
                document.getElementById("mensaje_final").innerHTML = respuesta.mensaje;
            },
            error: function (error){
                console.log(error);
            }
        })
    } else{
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/trigliceridos",
            data: JSON.stringify(trigliceridos),
            headers: {
                "accept": "application/json",
                "content-type": "application/json"
            },
            success: function (respuesta) {
                console.log(respuesta);
                
                document.getElementById("mensaje_final").innerHTML = respuesta.mensaje;
            },
            error: function (error){
                console.log(error);
            }
        })
    }

}