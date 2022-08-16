from pydantic import BaseModel
from enum import Enum


class Language(Enum):
    spanish="Español"
    english="Inglés"
    portuguese="Portugués"
    french="Francés"
    italian="Italiano"
    other="Otro"