from fastapi import FastAPI, Response, Depends
from src.core.config import get_settings, Settings

app = FastAPI(title="AI for Couples", description="一款为了解决情侣之间不必要矛盾的神器")

@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return {
        "message": "Hello from the {settings.app_name}!",
        "database_url": settings.database_url,
        "jwt_secret": settings.jwt_secret
        }

@app.get("/health")
async def health_check(response: Response):
    response.status_code = 200
    return {"status": "Healthy✅"}



if __name__ == "__main":
    import uvicorn
    uvicorn.run("src.main:app", host="localhost", port=8000, reload=True)