function habilitarNotas(materia){
    var fila = document.getElementById(materia);
    var notas = fila.querySelectorAll(".nota");
    var checkbox = fila.querySelector('input[type="checkbox"]');
    var botonPromedio = fila.querySelector("input[type='button']");

    if ( checkbox.checked){
        notas.forEach(nota => {
            nota.disabled = false
        });
    } else {
        notas.forEach( nota => nota.disabled = true)
    }
}