import os
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# Leer la API Key desde la variable de entorno
API_KEY = os.getenv("API_KEY", "default_key")

# Imprimir la API Key en uso (solo para depuración)
print(f"🔍 DEPURACIÓN: La API_KEY en uso es: {API_KEY}")

@app.get("/")
def read_root(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
    return {"message": "✅ API deployed successfully on Render with Authentication!"}
