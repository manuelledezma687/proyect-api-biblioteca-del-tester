from fastapi import Form
from pydantic import BaseModel, Field, EmailStr


class Contact(BaseModel):
    first_name: str = Field(
        ...,
        max_length=20,
        example="Manuel Ledezma"
        )
    email: EmailStr = Field(
        ...,
        example="testing@gmail.com"
        )
    comments: str = Field(
        ...,
        max_length=100,
        example="Hola estoy interesado en participar en el programa de incentivos de la págiona."
        )
    
class MessageSend(BaseModel):
    message: str = Field(default="Envío de formulario exitoso")