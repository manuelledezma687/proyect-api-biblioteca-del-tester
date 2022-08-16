#Python
import json
from http import client

#Pydantic

#FastApi
from fastapi import status
from fastapi import Body
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import APIRouter

#Native Modules
from models.Courses import *


router = APIRouter()


## Cursos.
@router.get(
    path="/courses",
    status_code=status.HTTP_200_OK,
    summary="Mostrar un curso específico",
    tags=["Cursos"])
def show_courses():
    """
    ## This path operation shows all courses in the app

    Parameters: 
        -

    Returns a json list with all courses in the app, with the following keys: 
        - title: str
        - comments: str
        - resume: str
        - image: ImageStr
        - published: bool
    """
    with open("data/courses.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results

@router.post(
    path="/courses",
    response_model=Courses,
    status_code=status.HTTP_201_CREATED,
    summary="Postear un curso",
    tags=["Cursos"])
def post_course(course: PublishedCourse=Body(...)):
    """
    ## This path operation post a course in the app

    Parameters: 
        -course: PublishedCourse

    Returns a json list with the created course in the app, with the following keys: 
        - title: str
        - comments: str
        - resume: str
        - image: ImageStr
        - published: bool
    """
    with open("data/courses.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        courses_dict = course.dict()
        courses_dict["created_at"] = str(courses_dict["created_at"])
        courses_dict["updated_at"] = str(courses_dict["updated_at"])
        results.append(courses_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return course