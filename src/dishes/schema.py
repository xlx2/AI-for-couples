from datetime import datetime
from pydantic import BaseModel, Field


class DishBase(BaseModel):
    """ Dish公共字段基类 """
    name: str = Field(..., max_length=255, description="菜品名称")
    description: str|None = Field(None, description="菜品描述")

class DishCreate(DishBase):
    """ 用于创建模型 """
    pass

class DishUpdate(DishBase):
    """ 用于更新模型 """
    name: str|None = Field(None, max_length=255, description="菜品名称")
    description: str|None = Field(None, description="菜品描述")

class DishResponse(DishBase):
    """ 响应模型 """
    id: int
    created_at: datetime
    model_config = {
        "from_attributes": True
    }