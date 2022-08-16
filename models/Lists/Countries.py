from pydantic import BaseModel
from enum import Enum


class Countries(Enum):
    Argentina = "Argentina"
    Bolivia = "Bolivia"
    Peru = "Perú"
    Paraguay = "Paraguay"
    Mexico = "México"
    Venezuela = "Venezuela"
    USA = "Estados Unidos"
    Colombia ="Colombia"
    Chile ="Chile"
    Panama ="Panamá"
    Costa_Rica ="Costa Rica"
    El_Salvador ="El Salvador"
    Resto_del_Mundo = "Resto del Mundo"