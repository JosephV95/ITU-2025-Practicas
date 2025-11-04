document.addEventListener("DOMContentLoaded", () => {
  const tabla = document.querySelector("#tabla-materias tbody");
  const btnValidar = document.getElementById("btnValidar");
  const resultado = document.getElementById("resultado");

  // Generar 10 filas vacías
  for (let i = 0; i < 10; i++) {
    const fila = document.createElement("tr");
    fila.innerHTML = `
      <td><input type="text" placeholder="Materia ${i + 1}"></td>
      <td><input type="number" min="0" max="10" placeholder="0-10"></td>
    `;
    tabla.appendChild(fila);
  }

  btnValidar.addEventListener("click", () => {
    const datos = obtenerDatosPersonales();
    const materias = obtenerMaterias();

    if (!validarDatosPersonales(datos)) return;
    if (!validarMaterias(materias)) return;
    if (!validarPromedio(materias)) return;

    resultado.style.color = "green";
    resultado.textContent = `✅ Datos correctos. El alumno ${datos.nombre} ${datos.apellido} cumple los requisitos.`;
  });
});

function obtenerDatosPersonales() {
  return {
    nombre: document.getElementById("nombre").value.trim(),
    apellido: document.getElementById("apellido").value.trim(),
    dni: document.getElementById("dni").value.trim(),
    domicilio: document.getElementById("domicilio").value.trim(),
    fechaNacimiento: document.getElementById("fechaNacimiento").value
  };
}

function obtenerMaterias() {
  const filas = document.querySelectorAll("#tabla-materias tbody tr");
  const materias = [];

  filas.forEach(fila => {
    const materia = fila.children[0].querySelector("input").value.trim();
    const nota = Number(fila.children[1].querySelector("input").value);
    if (materia && !isNaN(nota)) {
      materias.push({ materia, nota });
    }
  });

  return materias;
}

function validarDatosPersonales({ nombre, apellido, dni, domicilio, fechaNacimiento }) {
  const resultado = document.getElementById("resultado");

  if (!nombre || !apellido || !dni || !domicilio || !fechaNacimiento) {
    resultado.style.color = "red";
    resultado.textContent = "⚠️ Complete todos los datos personales.";
    return false;
  }

  const fecha = new Date(fechaNacimiento);
  const hoy = new Date();
  const edad = hoy.getFullYear() - fecha.getFullYear();

  if (fecha > hoy || edad < 5 || edad > 100) {
    resultado.style.color = "red";
    resultado.textContent = "⚠️ La fecha de nacimiento no es lógica.";
    return false;
  }

  return true;
}

function validarMaterias(materias) {
  const resultado = document.getElementById("resultado");

  if (materias.length < 5) {
    resultado.style.color = "red";
    resultado.textContent = "⚠️ El alumno debe haber cursado al menos 5 materias.";
    return false;
  }

  return true;
}

function validarPromedio(materias) {
  const resultado = document.getElementById("resultado");
  const promedio = materias.reduce((acc, m) => acc + m.nota, 0) / materias.length;

  if (promedio < 7) {
    resultado.style.color = "red";
    resultado.textContent = `⚠️ El promedio general (${promedio.toFixed(2)}) es inferior a 7.`;
    return false;
  }

  return true;
}
