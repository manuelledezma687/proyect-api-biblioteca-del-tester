#Python
from typing import Optional
from datetime import date
from datetime import datetime

#Pydantic
from pydantic import BaseModel, Field


class Courses(BaseModel):
    teacher: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Manuel Ledezma"
        )
    title: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Curso de Postman"
        )
    resume: str = Field(
        ...,
        min_length=1,
        max_length=200,
        example="Hola este es una muestra de una breve descripción"
        )
    # tags: str 
    image: str
    published: bool = Field(default=None, example=False)
    
class PublishedCourse(Courses):
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)