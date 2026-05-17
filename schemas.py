from typing import List
from pydantic import BaseModel, Field


class IngredientBase(BaseModel):
    name: str = Field(..., examples=["Мука"])


class IngredientCreate(IngredientBase):
    pass


class IngredientOut(IngredientBase):
    id: int

    model_config = {"from_attributes": True}


class RecipeBase(BaseModel):
    name: str = Field(..., examples=["Овсяная каша"])
    cooking_time: int = Field(..., gt=0, examples=[15])
    description: str = Field(default="", examples=["Простое и полезное блюдо"])


class RecipeCreate(RecipeBase):
    ingredients: List[str] = Field(
        ..., examples=[["Овсяные хлопья", "Молоко", "Вода", "Соль"]]
    )


class RecipeListOut(BaseModel):
    """Поля для экрана со списком рецептов"""

    id: int
    name: str
    views: int
    cooking_time: int

    model_config = {"from_attributes": True}


class RecipeDetailOut(RecipeBase):
    """Детальная информация о рецепте"""

    id: int
    views: int
    ingredients: List[IngredientOut]

    model_config = {"from_attributes": True}