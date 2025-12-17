from fastapi import FastAPI, Response, Depends

from src.core.config import settings
from src.lifespan import lifespan
from src.core.exception import register_exception_handlers
from src.dishes.router import router as dish_router

app = FastAPI(
    title=settings.app_name, 
    version="0.1.0",
    description="一款为了解决情侣之间矛盾的工具",
    lifespan=lifespan
    )

register_exception_handlers(app)

# 注册路由
app.include_router(dish_router)

@app.get("/")
async def root():
    return {
        "message": f"Hello from the {settings.app_name}!",
        "database_url": settings.database_url,
        "jwt_secret": settings.jwt_secret
        }

@app.get("/health")
async def health_check(response: Response):
    response.status_code = 200
    return {"status": "Healthy✅"}
