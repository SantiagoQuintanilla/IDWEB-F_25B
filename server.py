from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import os
import mimetypes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

def application(environ, start_response):
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]

    if path == "/sugerencias" and method == "POST":
        content_length = int(environ.get("CONTENT_LENGTH", 0))
        body = environ["wsgi.input"].read(content_length).decode("utf-8")
        data = parse_qs(body)

        nombre = data.get("nombre", [""])[0]
        correo = data.get("correo", [""])[0]
        asunto = data.get("asunto", [""])[0]
        mensaje = data.get("mensaje", [""])[0]

        archivo = os.path.join(BASE_DIR, "sugerencias.txt")
        print("POST /sugerencias recibido")
        with open(archivo, "a", encoding="utf-8") as f:
            f.write("---- Nueva sugerencia ----\n")
            f.write(f"Nombre: {nombre}\n")
            f.write(f"Correo: {correo}\n")
            f.write(f"Tipo: {asunto}\n")
            f.write(f"Mensaje: {mensaje}\n\n")

        start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
        return [b"""
            <h2>Gracias por tu sugerencia</h2>
            <a href="/static/index.html">Volver al inicio</a>
        """]
    
    if path.startswith("/static/"):
        file_path = os.path.join(BASE_DIR, path.lstrip("/"))

        if os.path.exists(file_path):
            content_type, _ = mimetypes.guess_type(file_path)
            content_type = content_type or "application/octet-stream"

            with open(file_path, "rb") as f:
                content = f.read()

            start_response("200 OK", [("Content-Type", content_type)])
            return [content]

    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Recurso no encontrado"]

if __name__ == "__main__":
    print("Servidor activo en http://localhost:8000/static/index.html")
    server = make_server("", 8000, application)
    server.serve_forever()