#Python
from os import stat
import json
from uuid import UUID
from datetime import date
from datetime import datetime
from enum import Enum
from typing import Optional, List

#Pydantic
from pydantic import EmailStr

#FastApi
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Query, Path, Form
from fastapi import HTTPException

#Native Modules
from models.Course import Course, CourseCreated
from models.User import *
from models.Contact import Contact, MessageSend

app= FastAPI()

## Home
@app.get(path="/", 
         status_code=status.HTTP_200_OK , 
         summary="Home del sitio web",
         tags=["Biblioteca del Tester"])
def home():
    """
    # Home del Sitio web Biblioteca del Tester.
    ## Taxonomia del sitio web:
        -Usuarios: 
            Login. (path=/login)
            Registro.  (path=/users/new)
            Actualización.  (path=/users/user_id)
            Borrado de usuario. (path=/users/user_id)
            Mostrar un usuario.  (path=/users/user_id)
            Mostrar todos los usuarios.  (path=/users, filters= country, id, name, limit)
        -Cursos: 
            Mostrar un curso.  (path=/course_id)
            Mostrar todos los cursos.  (path=/courses)
            Publicar un curso.  (path=/courses)
            Actualizar un curso.  (path=/course_id)
            Borrar un curso.  (path=/course_id)
        -Comentarios: 
            Mostrar todos los comentarios.  (path=/comments)
            Mostrar un comentario.  (path=/comment/id)
            Actualizar un comentario.  (path=/comment/id)
            Postear un comentario.  (path=/course_id/comments)
            Borrar un comentario. (path=/comment/id)
        -Publicación de Empleos: 
            Mostrar todas las vacantes. (path=/jobs)
            Mostrar una sola vacante por filtro. (path=/jobs, filter=country, remote or local, type_of_work)
            Postear una vacante. (path=/job)
            Modificar una vacante. (path=/job_id)
            Borrar una vacante.(path=/job_id)
        -Contacto directo: 
            Enviar un mensaje al equipo de bibliotecadeltester.org. (path=/contact)
    """
    return("Hola Bienvenido a Biblioteca del Tester")

## 1 Usuarios
@app.post(
    path="/login",
    response_model=UserLogin,
    status_code=status.HTTP_200_OK,
    summary="Ingreso de Usuario",
    tags=["Usuarios"])
def login(user: UserLogin = Body(...)):
    """
    ## Login User

    This path operation is for login user.

    Parameters: 
        - Request body parameter
            - user: UserLogin
    
    Returns a message confirmation.
    """
    return UserLoginOk(message=message)

@app.post(
    path="/users/new", 
    response_model=User,
    status_code=status.HTTP_201_CREATED, 
    summary="Registro de Usuario",
    tags=["Usuarios"])

def post_user(user: UserRegister=Body(...)):
    """
    ## Signup

    This path operation register a user in the app

    Parameters: 
        - Request body parameter
            - user: UserRegister
    
    Returns a json with the basic user information: 
        - user_id: UUID
        - email: Emailstr
        - username: str
        - first_name: str
        - last_name: str
        - age: int
        - country: List Optional
        - language: List Optional
        - Ocupation: str
    """
    
    with open("users.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user
        ##if any(users['email'] == user.email for users in results):
        ##    raise HTTPException(
        ## status_code=status.HTTP_409_CONFLICT,
        ## detail="Email already exist!")

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Mostrar Usuarios",
    tags=["Usuarios"]
)
def show_users():
    """
    ## This path operation shows all users in the app

    Parameters: 
        -

    Returns a json list with all users in the app, with the following keys: 
        - user_id: UUID
        - email: Emailstr
        - username: str
        - first_name: str
        - last_name: str
        - age: int
        - country: List Optional
        - language: List Optional
        - Ocupation: str
    """
    with open("users.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results
    
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Mostrar un Usuario",
    tags=["Usuarios"]
)
def show_a_user():
    """
    ## This path operation shows an user in the app

    Parameters: 
        - 

    Returns a json list with all users in the app, with the following keys: 
        - user_id: UUID
        - email: Emailstr
        - username: str
        - first_name: str
        - last_name: str
        - age: int
        - country: List Optional
        - language: List Optional
        - Ocupation: str
    """
    pass

@app.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Actualizar un Usuario",
    tags=["Usuarios"]
)
def update_a_user(user: UserRegister=Body(...)): 
    """
    ## This path operation update an user in the app

    Parameters: 
        - 

    Returns a json list with all users in the app, with the following keys: 
        - user_id: UUID
        - email: Emailstr
        - username: str
        - first_name: str
        - last_name: str
        - age: int
        - country: List Optional
        - language: List Optional
        - Ocupation: str
    """
    pass

@app.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Borrar un Usuario",
    tags=["Usuarios"]
)
def delete_a_user(): 
    """
    ## This path operation delete an user in the app

    Parameters: 
        - 

    Returns a json list with all users in the app, with the following keys: 
        - user_id: UUID
        - email: Emailstr
        - username: str
        - first_name: str
        - last_name: str
        - age: int
        - country: List Optional
        - language: List Optional
        - Ocupation: str
    """
    pass

## Contacto Directo
@app.post(
    path="/contact", 
    status_code=status.HTTP_201_CREATED, 
    summary="Formulario de contacto",
    tags=["Contacto Directo"])
def contact(
    name: str=Form(
        ...,
        min_length=5,
        max_length=20),
    email: EmailStr = Form(...), 
    comments: str =Form(
        ...,
        min_length=5,
        max_length=250)):
    """
    ## This path operation is for contact with bibliotecadeltester.org

    - Request body parameter
        - **Form**:
            mane: str
            email: EmailStr
            comments: str

    Returns a message confirmation: 
        
        - "Muchas gracias por enviar tu mensaje, en breve nos contactaremos contigo."
    """
    return ("Muchas gracias por enviar tu mensaje, en breve nos contactaremos contigo.")