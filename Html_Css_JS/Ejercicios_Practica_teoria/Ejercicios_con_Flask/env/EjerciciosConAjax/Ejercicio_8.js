function comprobarCampos() {
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var dni = document.getElementById("dni").value;
    var nacimiento = document.getElementById("nacimiento").value;
    if (nombre === "" || apellido === "" || dni === "" || nacimiento === "") {
        alert("Complete todos los campos obligatorios.");
        return false;
    }
}
function obtenerPromedio() {
    // comprobarCampos();
    var nota1 = document.getElementById("nota_1").value;
    var nota2 = document.getElementById("nota_2").value;
    var nota3 = document.getElementById("nota_3").value;
    var nota4 = document.getElementById("nota_4").value;
    var nota5 = document.getElementById("nota_5").value;

    var dataNotas = {"nota1": nota1, "nota2": nota2, "nota3": nota3, "nota4": nota4, "nota5": nota5 };
    console.log(dataNotas);

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/promedio",
        data: JSON.stringify(dataNotas),
        headers: {
            "accept": "application/json",
            "content-type": "application/json",
        },

        success: function (response) {
            document.querySelector(".mensaje_promedio").innerHTML =
             "El promedio es: " + response.promedio + " y la nota mas alta es: " + response.nota_mas_alta;
        },
        error: function (error) {
            console.log(error);
        },
    });

    // Funciones para manejar las fechas con JavaScript, PERO EL EJERCICIO PIDE HACERLO CON FLASK
    // // Crear objeto Date con la fecha de nacimiento
    // const fechaNacimiento = new Date(nacimiento);
    // // Obtener la fecha actual
    // const hoy = new Date();
    // // Calcular la edad
    // let edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
    // const mes = hoy.getMonth() - fechaNacimiento.getMonth();
    // // Ajuste si el cumpleaños aún no llegó este año
    // if (mes < 0 || (mes === 0 && hoy.getDate() < fechaNacimiento.getDate())) {
    //     edad--;
    // }
}

function verificarEdad() {
    // comprobarCampos();
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var nacimiento = document.getElementById("nacimiento").value;
  
    var dataEdad = { "nacimiento": nacimiento };
    console.log(dataEdad);

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/verificar_edad",
        data: JSON.stringify(nacimiento),
        headers: {
        "accept": "application/json",
        "content-type": "application/json",
        },

        success: function (response) {
            data_recibida = response;
            mensaje_final = `El alumno ${nombre} ${apellido} ${data_recibida.mensaje} Tiene ${data_recibida.edad} años.`;
            document.querySelector(".mensaje_edad").innerHTML = mensaje_final;
        },
        error: function (error) {
            console.log("Ocurrio un error: ", error);
        },
    });
}
