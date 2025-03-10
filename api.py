from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilitar CORS para que otros sitios puedan acceder a la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes especificar la URL de GitHub Pages si quieres más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint para la API
@app.get("/nombres")
async def obtener_nombres():
    return ["Juan", "María", "Pedro"]

# Endpoint para servir la página HTML
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()
