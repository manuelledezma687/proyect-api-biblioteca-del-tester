#Python packages

#Pydantic packages

#FastAPI packages
from fastapi import FastAPI

#Local packages
from paths import Home, Courses,Users, Comments, Contact

app = FastAPI()

#Paths from the proyect.
app.include_router(Home.router)
app.include_router(Courses.router)
app.include_router(Users.router)
app.include_router(Comments.router)
app.include_router(Contact.router)