from pydantic import BaseModel, Field
from typing import Optional


class Course(BaseModel):
    course_id: int = Field(
        ...,
        gt=0,
        example=12
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
    published: bool = Field(default=None, example=False)
    teacher: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Manuel Ledezma"
        )
    
class CourseCreated(Course):
    message: str=Field(default="Curso creado con éxito")