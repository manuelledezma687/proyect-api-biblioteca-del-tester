from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from models.Countries import Countries
from models.Language import Language


class UserBase(BaseModel):
    name: str = Field(
        ...,
        min_length=0,
        max_length=50,
        example="Manuel"
        )
    last_name: str = Field(
        ...,
        min_length=0,
        max_length=50,
        example="Ledezma"
        )
    age: int = Field(
        ...,
        gt=15,
        le=99,
        example=34
        )
    ocupation: str = Field(
        min_length=0,
        max_length=50,
        example="Ingeniero en Pruebas"
        )
    email = str
    country: Optional[Countries]
    language: Optional[Language]
    
class User(UserBase):
        password: str = Field(
        ...,
        min_length=12,
        example="Hidden"
        ) 

class UserResponse(UserBase):
    pass