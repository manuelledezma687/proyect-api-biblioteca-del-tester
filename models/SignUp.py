from fastapi import Form
from pydantic import BaseModel, Field, EmailStr


class SignUp(BaseModel):
    name: str = Field(
        ...,
        max_length=20,
        example="Manuel"
        )
    email: EmailStr = Field(
        ...,
        example="Ledezma@gmail.com"
        )
    message: str=Field(default="Login exitoso")
    

class SignUpResponse(SignUp):
    password: str = Field(
    ...,
    max_length=12,
    example="Hidden"
    )
