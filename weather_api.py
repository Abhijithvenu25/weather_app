from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Define the base URL and API key for your weather API provider
WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1/"
WEATHER_API_KEY = "b47bea4061204898ae3111653241305"

# Endpoint to get weather forecast by city name
@app.get("/weather/{city}")
async def get_weather(city: str):
    print('in line 13')
    url = f"{WEATHER_API_BASE_URL}/current.json?key={WEATHER_API_KEY}&q={city}&days=1"
    print('url:',url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Weather data not found")
    
@app.get('/')
def about():
    return {'test weather'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=1234)

# 'http://api.weatherapi.com/v1/current.json?key=b47bea4061204898ae3111653241305&q=London&aqi=no'