#Python
from typing import Optional
from datetime import date
from datetime import datetime
from uuid import UUID

#Pydantic
from pydantic import BaseModel, Field

class Comments(BaseModel):
    post_id: UUID = Field(...)
    comment: str = Field(
        ..., 
        min_length=1,
        max_length=500,
        example="Hola quisiera participar en el bootcamp de Junio."
        )
    created_at: datetime = Field(default=datetime.now())