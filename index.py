import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

# Importamos los controladores (Routers)
from src.feature.chat.infraestructure.controller.ChatController import router as chat_router
from src.feature.generateActivity.infraestructure.controller.ActivityController import router as activity_router

# 1. Cargar variables de entorno del archivo .env
load_dotenv()

# 2. Inicializar la App
app = FastAPI(
    title="Clean Architecture AI Backend",
    description="Backend modular con Gemini API",
    version="1.0.0"
)

# 3. Registrar las rutas (Incluimos cada "feature")
app.include_router(chat_router)
app.include_router(activity_router)

# Ruta de prueba
@app.get("/")
def read_root():
    return {"status": "Servidor funcionando correctamente"}

# 4. Ejecución del servidor
if __name__ == "__main__":
    uvicorn.run("index:app", host="0.0.0.0", port=8000, reload=True)