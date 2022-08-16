#Python
import json
from typing import List,Optional
from http import client

#Pydantic

#FastApi
from fastapi import status
from fastapi import Body, Path
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import APIRouter

#Native Modules
from models.Courses import *
from models.Users import *
from models.Contact import Contact
from models.Comments import *


router = APIRouter()


## Comments.
@router.get(
    path="/comments",
    status_code=status.HTTP_200_OK,
    summary="Mostrar todos los comentarios",
    tags=["Comentarios"])
def show_comments():
    """
    ## This path operation shows all comments in the app.

    Parameters: 
        -

    Returns a json list with all comments in the app, with the following keys: 
        - comments: str
    """
    with open("data/posts.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results

@router.post(
    path="/comments",
    response_model=Comments,
    status_code=status.HTTP_201_CREATED,
    summary="Postear un comentario",
    tags=["Comentarios"])
def post_comments(comment: Comments=Body(...)):
    """
    ## This path operation post a course in the app.

    Parameters: 
        -comments: Comments

    Returns a created comment in the app, with the following keys: 
        - comments: str
        - Created: datetime Field

    """
    with open("data/posts.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        comments_dict = comment.dict()
        comments_dict["post_id"] = str(comments_dict["post_id"])
        comments_dict["created_at"] = str(comments_dict["created_at"])
        results.append(comments_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return comment
    
@router.delete(
    path="/comments/{post_id}",
    status_code=status.HTTP_200_OK,
    summary="Borrar un comentario",
    tags=["Comentarios"])
def delete_comment(post_id: UUID):
    """
    ## This path operation delete a comment in the app.

    Parameters: 
        -post_id: str

    Returns a json Response with the result for this operation.

    """
    try:
        return JSONResponse(status_code=200, content={'message': "Recurso eliminado"})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={'message': "Ha ocurrido un error"})

