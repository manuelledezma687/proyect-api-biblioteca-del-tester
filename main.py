from os import stat
from fastapi import FastAPI
from fastapi import status
from typing import Optional
from pydantic import BaseModel, Field
from fastapi import Body, Query, Path, Form
from enum import Enum
from models.Course import Course, CourseCreated
from models.User import User, UserResponse
from starlette.types import Message
from models.Login import LoginOut
from models.Contact import Contact
from models.SignUp import SignUp, SignUpResponse

app= FastAPI()

## 1.1 Home
@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return("Hola Bienvenido a Biblioteca del Tester")

## 1.2 Cursos disponibles
@app.get("/courses/{course_id}", status_code=status.HTTP_200_OK)
def courses(course: Course =Body(...)):
    return course

@app.get("/courses/detail/{course_id}")
def show_course(
    course_id: int = Path(
        ...,
        title= "Course Id",
        description="Esto es un ID de un curso y es mayot a cero.",
        gt=0
        ),

):
    return {curso_id: "It exists!"}

@app.post("/courses", response_model=CourseCreated,status_code=status.HTTP_201_CREATED)
def post_course(course: Course=Body(...)):
    return course

## Perfil de usuario
@app.get("/profile/{user_id}", status_code=status.HTTP_200_OK)
def get_profile(user: User=Body(...)):
    return user

@app.post("/profile/new", response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def post_profile(user: User=Body(...)):
    return user


## Login de usuario
@app.post("/login", response_model=LoginOut, status_code=status.HTTP_200_OK)
def login(username: str = Form(...), password: str = Form(...)):
    return LoginOut(username=username)


## Registro de usuario
@app.post("/signup", response_model=SignUpResponse, status_code=status.HTTP_201_CREATED)
def new_user(name: str=Form(...), email: str = Form(...), password: str =Form(...)):
    return SignUp(message=message)


## Contacto Directo
@app.post("/contact", response_model=Contact, status_code=status.HTTP_201_CREATED)
def contact(name: str=Form(...), email: str = Form(...), comments: str =Form(...)):
    return Contact(message=message)


## Faltan los put and delete de los servicios.