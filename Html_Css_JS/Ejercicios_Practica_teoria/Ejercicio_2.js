function mostrarImpares() {
  let num_minimo = parseInt(document.getElementById("num_minimo").value) ; //?  Se debe convertir a numero con parseInt, porque desde input se reciben como texto
  let num_maximo = parseInt(document.getElementById("num_maximo").value) ; //?  Se debe convertir a numero con parseInt, porque desde input se reciben como texto

  let lista_impares = [];

  for (let i = num_minimo ; i <= num_maximo ; i++) {
    
    if (i % 2 != 0){
        lista_impares.push(i)
    }
  }

  alert(`Entre los numeros ${num_minimo} y ${num_maximo}, los numeros impares son: 
    \n ${lista_impares.join(", ")}`)
}
 