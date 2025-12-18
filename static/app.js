document.addEventListener("DOMContentLoaded", () => {
  const formulario = document.querySelector(".formulario-contacto");

  if (formulario) {
    formulario.addEventListener("submit", (e) => {
      e.preventDefault();

      const nombre = document.getElementById("nombre").value.trim();
      const correo = document.getElementById("correo").value.trim();
      const asunto = document.getElementById("asunto").value.trim();
      const mensaje = document.getElementById("mensaje").value.trim();

      if (nombre.length < 3) {
        alert("El nombre debe tener al menos 3 caracteres.");
        return;
      }

      if (!correo.includes("@") || !correo.includes(".")) {
        alert("Ingrese un correo electrónico válido.");
        return;
      }

      if (asunto.length < 4) {
        alert("El asunto debe ser más descriptivo.");
        return;
      }

      if (mensaje.length < 10) {
        alert("El mensaje debe tener al menos 10 caracteres.");
        return;
      }

      alert("Gracias por tu sugerencia. Tu mensaje ha sido enviado.");

      formulario.reset();
    });
  }
});
document.addEventListener("DOMContentLoaded", () => {
  const filtro = document.getElementById("filtro-genero");
  const albums = document.querySelectorAll(".card-album");

  if (filtro) {
    filtro.addEventListener("change", () => {
      const generoSeleccionado = filtro.value;

      albums.forEach((album) => {
        const generosAlbum = album.dataset.genero.split(" ");

        if (
        generoSeleccionado === "todos" ||
        generosAlbum.includes(generoSeleccionado)
        ) {
        album.style.display = "block";
        } else {
        album.style.display = "none";
        }
      });
    });
  }
});
