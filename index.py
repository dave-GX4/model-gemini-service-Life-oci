import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from src.feature.chat.infraestructure.controller.ChatController import router as chat_router
from src.feature.generateActivity.infraestructure.controller.ActivityController import router as activity_router

load_dotenv()

app = FastAPI(
    title="Clean Architecture AI Backend",
    description="Backend modular con Gemini API",
    version="1.0.0"
)

app.include_router(chat_router)
app.include_router(activity_router)

@app.get("/ServerGemini")
def read_root():
    return {"status": "Servidor funcionando correctamente"}

if __name__ == "__main__":
    uvicorn.run("index:app", host="0.0.0.0", port=8000, reload=True)