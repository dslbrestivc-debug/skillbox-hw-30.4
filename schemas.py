from typing import List

from pydantic import BaseModel, Field


# ---- Ингредиент ----
class IngredientBase(BaseModel):
    name: str = Field(..., example="Мука")


class IngredientCreate(IngredientBase):
    pass


class IngredientOut(IngredientBase):
    id: int

    class Config:
        from_attributes = True


# ---- Рецепт ----
class RecipeBase(BaseModel):
    name: str = Field(..., examples="Овсяная каша")
    cooking_time: int = Field(..., gt=0, examples=15)
    description: str = Field(default="", examples="Простое и полезное блюдо")


class RecipeCreate(RecipeBase):
    ingredients: List[str] = Field(
        ..., examples=["Овсяные хлопья", "Молоко", "Вода", "Соль"]
    )


class RecipeListOut(BaseModel):
    """Поля для экрана со списком рецептов"""

    id: int
    name: str
    views: int
    cooking_time: int

    class Config:
        from_attributes = True


class RecipeDetailOut(RecipeBase):
    """Детальная информация о рецепте"""

    id: int
    views: int
    ingredients: List[IngredientOut]

    class Config:
        from_attributes = True
