import os
import logging
from fastapi import FastAPI, Header, HTTPException, Depends

# Configuración de logs
logging.basicConfig(level=logging.INFO)

# Inicialización de la API
app = FastAPI(
    title="FinZen AI - Global Finance API",
    description="API para optimización financiera con inteligencia artificial.",
    version="1.0.0"
)

# Verificar que API_KEY esté configurada correctamente
API_KEY = os.getenv("API_KEY", "").strip()

if not API_KEY:
    logging.warning("⚠️ WARNING: API_KEY no está configurada en las variables de entorno. La API funcionará, pero los endpoints protegidos no estarán accesibles.")

# Middleware para validación de API Key
def validate_api_key(x_api_key: str = Header(...)):
    if x_api_key.strip() != API_KEY:
        raise HTTPException(status_code=401, detail="❌ Unauthorized: Invalid API Key")
    return x_api_key

# Endpoint de prueba
@app.get("/ping", summary="Health Check")
def health_check():
    logging.info("✅ Health check solicitado.")
    return {"status": "OK", "message": "API is running successfully"}

# Endpoint protegido con API Key
@app.get("/", summary="Endpoint Protegido", dependencies=[Depends(validate_api_key)])
def read_root():
    logging.info("🔐 Acceso autorizado a la API.")
    return {"message": "API deployed successfully!"}
    if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
