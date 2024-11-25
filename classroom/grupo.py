from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 6"  # Valor inicial por defecto

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas else []
        self.listadoAlumnos = estudiantes if estudiantes else []

    def agregarAlumno(self, alumno, lista=[]):
        lista.append(alumno)
        self.listadoAlumnos.extend(lista)  # Agregar los nuevos alumnos a la lista

    def listadoAsignaturas(self, **kwargs):
        for nombre in kwargs.values():
            self._asignaturas.append(Asignatura(nombre))  # Crear asignaturas con los nombres pasados

    def __str__(self):
        alumnos_str = ", ".join(self.listadoAlumnos)
        return f"Grupo de estudiantes: {self._grupo} ({alumnos_str})"

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre