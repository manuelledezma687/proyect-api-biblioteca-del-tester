from pydantic import BaseModel, Field

class LoginOut(BaseModel):
    username: str = Field(
        ...,
        max_length=20,
        example="Manuel"
        )
    message: str=Field(default="Login exitoso")