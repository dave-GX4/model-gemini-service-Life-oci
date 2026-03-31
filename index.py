import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from src.feature.generateActivity.infraestructure.controller.ActivityController import router as activity_router

if os.getenv("RAILWAY_ENVIRONMENT") is None:
    load_dotenv()

app = FastAPI(
    title="Clean Architecture AI Backend",
    description="Backend modular con Gemini API",
    version="1.0.0"
)

app.include_router(activity_router)

@app.get("/ServerGemini")
def read_root():
    return {"status": "Servidor funcionando correctamente"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("index:app", host="0.0.0.0", port=port, reload=False)