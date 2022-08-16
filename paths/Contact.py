#Python
import json
from http import client

#Pydantic
from pydantic import EmailStr

#FastApi
from fastapi import status
from fastapi import Form
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import APIRouter

#Native Modules
from models.Contact import Contact


router = APIRouter()


## Contacto Directo.
@router.post(
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
    ## This path operation is for direct contact with bibliotecadeltester.org

    - Request body parameter
        - **Form**:
            mane: str
            email: EmailStr
            comments: str

    Returns a message confirmation: 
        - "Muchas gracias por enviar tu mensaje, en breve nos contactaremos contigo."
        
    """
    return JSONResponse(status_code=201, content={'message': "Muchas gracias por enviar tu mensaje, en breve nos contactaremos contigo."})