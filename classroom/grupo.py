class grupo:
    grado = "Grado 6"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas else []
        self.listadoAlumnos = estudiantes if estudiantes else []

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos.extend(lista)

    def listadoAsignaturas(self, **kwargs):
        for nombre in kwargs.values():
            self._asignaturas.append(asignatura(nombre))

    def __str__(self):
        alumnos_str = ", ".join(self.listadoAlumnos)
        return f"Grupo de estudiantes: {self._grupo} ({alumnos_str})"  # Este formato debe ser exacto

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre