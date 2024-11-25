from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="Grupo ordinario", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = estudiantes if estudiantes is not None else []

    def listadoAsignaturas(self, asignaturas_dict):
        for nombre, salon in asignaturas_dict.items():
            self._asignaturas.append(Asignatura(nombre, salon))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos += lista

    def __str__(self):
        asignaturas_str = ', '.join([str(asig) for asig in self._asignaturas])
        alumnos_str = ', '.join(self.listadoAlumnos)
        return f"Grupo: {self._grupo}\nAsignaturas: {asignaturas_str}\nAlumnos: {alumnos_str}"

    @classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre