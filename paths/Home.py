#Python
import json
from typing import List

#Pydantic

#FastApi
from fastapi import status
from fastapi import APIRouter

#Native Modules
from models.Courses import *


router = APIRouter()


## Home
@router.get(path="/", 
         status_code=status.HTTP_200_OK , 
         response_model=List[Courses],
         summary="Home del sitio web",
         tags=["Biblioteca del Tester"])
def home():
    """
    # Home del Sitio web Biblioteca del Tester.
    ## Servicios del sitio web:
        -Usuarios: 
            Login.
            Registro.
            Actualización.
            Borrado de usuario.
            Mostrar un usuario.
            Mostrar todos los usuarios.
        -Cursos: 
            Mostrar un curso.
            Mostrar todos los cursos.
            Publicar un curso.
            Actualizar un curso.
            Borrar un curso. 
        -Comentarios: 
            Mostrar todos los comentarios.
            Mostrar un comentario.
            Postear un comentario. 
            Borrar un comentario.
        -Contacto directo: 
            Enviar un mensaje al equipo de bibliotecadeltester.org. (path=/contact)
    """
    with open("data/courses.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results