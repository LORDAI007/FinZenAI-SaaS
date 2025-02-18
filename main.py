import os
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# 🔐 Leer API Key desde variable de entorno
API_KEY = os.getenv("API_KEY", "default_key")  # Cambia "default_key" por algo seguro

@app.get("/")
def read_root(x_api_key: str = Header(None)):
    # 🛡️ Validar API Key
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")

    return {"message": "✅ API deployed successfully on Render with Authentication!"}
