from fastapi import Form
from pydantic import BaseModel, Field, EmailStr


class Contact(BaseModel):
    name: str = Field(
        ...,
        max_length=20,
        example="Manuel"
        )
    email: EmailStr = Field(
        ...,
        example="Ledezma@gmail.com"
        )
    comments: str = Field(
        ...,
        max_length=100,
        example="Hola esto es un comentario"
        )
    
    message: str=Field(default="Login exitoso")