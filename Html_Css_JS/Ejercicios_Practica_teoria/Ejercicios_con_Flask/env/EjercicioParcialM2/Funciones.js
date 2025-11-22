

function verificarCredito() {
  var valor_auto = document.getElementById("valor_auto").value;
  var ingreso_total = document.getElementById("ingreso").value;

  var informacion = { valor_auto: valor_auto, ingreso_total: ingreso_total };

  $.ajax({
    type: "POST",
    url: "http://127.0.0.1:5000/credito",
    data: JSON.stringify(informacion),
    headers: {
      accept: "application/json",
      "content-type": "application/json",
    },

    success: function (respuesta) {
      document.getElementById("mensaje_credito").innerHTML =
        respuesta.mensaje +
        " El credito maximo seria de: $" +
        respuesta.credito_max;
    },
    error: function (error) {
      console.log(error);
    },
  });
}

function verPromedio() {
  var ingreso = document.getElementById("ingreso").value;

  $.ajax({
    type: "POST",
    url: "http://127.0.0.1:5000/promedio",
    data: JSON.stringify(ingreso),
    headers: {
      accept: "application/json",
      "content-type": "application/json",
    },

    success: function (respuesta) {
      console.log(respuesta);

      document.getElementById("mensaje_promedio").innerHTML =
        "El promedio de ingresos es de: $" + respuesta.promedio;
    },
    error: function (error) {
      console.log(error);
    },
  });
}
