import os
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# Leer API Key desde las variables de entorno
API_KEY = os.getenv("API_KEY", "default_key").strip()

# Imprimir API Key almacenada en logs
print(f"🔍 DEPURACIÓN: API_KEY almacenada -> '{API_KEY}'")


@app.get("/ping")
def health_check():
    return {"status": "OK", "message": "API is running successfully"}


@app.get("/")
def read_root(x_api_key: str = Header(..., alias="x-api-key")):
    print(f"🔍 DEPURACIÓN: API Key recibida -> '{x_api_key}'")
    print(f"🔍 DEPURACIÓN: API_KEY almacenada -> '{API_KEY}'")
    print(f"🔍 Longitud x_api_key: {len(x_api_key)}, API_KEY: {len(API_KEY)}")
    print(f"🔍 x_api_key en bytes: {list(x_api_key.encode())}")
    print(f"🔍 API_KEY en bytes: {list(API_KEY.encode())}")

    if x_api_key.strip() != API_KEY:
        raise HTTPException(status_code=401, detail="❌ Unauthorized: Invalid API Key")
    
    return {"message": "✅ API deployed successfully on Render with Authentication!"}
