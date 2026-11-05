from fastapi import FastAPI, HTTPException
import requests
import os
import json
import redis
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Weather API with Redis Cache")

REDIS_URL = os.getenv("REDIS_URL", "redis://default:password@localhost:6379")
try:
    r = redis.from_url(REDIS_URL, decode_responses=True)
    r.ping()
    print("✅ Conectado a Redis")
except Exception as e:
    print(f"⚠️ No se pudo conectar a Redis: {e}. Usando caché en memoria.")
    r = None

memory_cache = {}

@app.get("/weather/{city}")
def get_weather(city: str):
    cache_key = f"weather:{city.lower()}"
    
    if r:
        cached = r.get(cache_key)
        if cached:
            return {"source": "redis_cache", "data": json.loads(cached)}
    elif cache_key in memory_cache:
        return {"source": "memory_cache", "data": memory_cache[cache_key]}

    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_res = requests.get(geo_url)
        geo_data = geo_res.json()
        
        if not geo_data.get("results"):
            raise HTTPException(status_code=404, detail="Ciudad no encontrada")
            
        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_res = requests.get(weather_url)
        weather_data = weather_res.json()
        
        result = {
            "city": city,
            "temperature": weather_data["current_weather"]["temperature"],
            "windspeed": weather_data["current_weather"]["windspeed"]
        }
        
        if r:
            r.setex(cache_key, 600, json.dumps(result))
        else:
            memory_cache[cache_key] = result
            
        return {"source": "live_api", "data": result}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
