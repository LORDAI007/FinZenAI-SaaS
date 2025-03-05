import os
from fastapi import FastAPI, Header, HTTPException

# Verificar que API_KEY esté configurada correctamente
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("❌ ERROR: API_KEY no está configurada en las variables de entorno.")

app = FastAPI()

# Endpoint de prueba
@app.get("/ping")
def health_check():
    return {"status": "OK", "message": "API is running successfully"}

# Endpoint protegido con API Key
@app.get("/")
def read_root(x_api_key: str = Header(...)):
    if x_api_key.strip() != API_KEY:
        raise HTTPException(status_code=401, detail="❌ Unauthorized: Invalid API Key")

    return {"message": "API deployed successfully!"}

