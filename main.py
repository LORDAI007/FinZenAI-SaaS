import os
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# Leer la API Key desde la variable de entorno
API_KEY = os.getenv("API_KEY", "default_key")

# Imprimir la API Key en uso (solo para depuración)
print(f"🔍 DEPURACIÓN: La API_KEY en uso es: {API_KEY}")

# 🚀 Endpoint principal (Verificar API Key)
@app.get("/")
def read_root(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
    return {"message": "✅ API deployed successfully on Render with Authentication!"}

# 🚀 Endpoint 2: Obtener información del sistema
@app.get("/status")
def get_status(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
    return {"status": "✅ Running", "version": "1.0.1", "environment": "production"}

# 🚀 Endpoint 3: Obtener información del usuario (ejemplo)
@app.get("/user/{user_id}")
def get_user(user_id: int, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
    return {"user_id": user_id, "name": "John Doe", "balance": 150.75}

# 🚀 Endpoint 4: Calcular suma de dos números (ejemplo de funcionalidad)
@app.get("/sum")
def calculate_sum(a: int, b: int, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
    return {"a": a, "b": b, "sum": a + b}
