import os
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# Leer API Key desde las variables de entorno
API_KEY = os.getenv("API_KEY", "default_key").strip()
print(f"🔍 DEPURACIÓN: API_KEY obtenida desde Vercel -> '{API_KEY}'")  # Depuración para verificar la API Key obtenida

# Endpoint de prueba
@app.get("/ping")
def health_check():
    return {"status": "OK", "message": "API is running successfully"}

# Endpoint protegido con API Key
@app.get("/")
def read_root(x_api_key: str = Header(...)):  # Eliminamos alias innecesario

    # Logs de depuración
    print(f"🔍 DEPURACIÓN: API Key recibida -> '{x_api_key}'")
    print(f"🔍 DEPURACIÓN: API_KEY almacenada -> '{API_KEY}'")
    print(f"📏 Longitud API Key recibida: {len(x_api_key)}, API_KEY esperada: {len(API_KEY)}")

    # Verificación de API Key
    if x_api_key.strip() != API_KEY:
        raise HTTPException(status_code=401, detail="❌ Unauthorized: Invalid API Key")

    return {"message": "✅ API deployed successfully!"}

