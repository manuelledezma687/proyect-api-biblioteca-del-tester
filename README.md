### Proyecto de Biblioteca del Tester.









@app.get(
    "/courses/detail/{course_id}"
    ,tags=["Cursos"])
def show_course(
    course_id: int = Path(
        ...,
        title= "Course Id",
        description="Esto es un ID de un curso y es mayot a cero.",
        gt=0
        ),

):
    return {curso_id: "It exists!"}

@app.post(
    path="/courses",
    response_model=CourseCreated,
    status_code=status.HTTP_201_CREATED,
    tags=["Cursos"])
def post_course(course: Course=Body(...)):
    return course




## Contacto Directo
@app.post(
    path="/contact", 
    response_model=Contact, 
    status_code=status.HTTP_201_CREATED, 
    tags=["Contacto"])
def contact(
    name: str=Form(...),
    email: str = Form(...), 
    comments: str =Form(...)):
    """
    ## Contacto Directo Con Nosotros.
    # Parametros:
        -Request Body parameter.
            -Contact: Contact
    """
    return MessageSend(message=message)


