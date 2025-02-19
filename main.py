import os
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# 🔐 Leer la API Key desde la variable de entorno 'API_KEY'
# Si no se encuentra en Render, usará "default_key"
API_KEY = os.getenv("API_KEY", "default_key")  

@app.get("/")
def read_root(x_api_key: str = Header(None)):
    # 🛡 Validar la API Key recibida en el header 'x-api-key'
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
    return {"message": "✅ API deployed successfully on Render with Authentication!"}
