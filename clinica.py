
from functools import reduce

from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion


class Clinica:

    def __init__(self):
        self._pacientes = []
        self._medicos = []
        self._citas = []
        self._historial = []

    # Verificar si un codigo ya existe
    def codigo_existe(self, codigo):
        if not isinstance(codigo, str):
            return False

        return self.buscar_por_codigo(codigo) is not None

    # Agregar paciente
    def agregar_paciente(self, paciente):
        if not isinstance(paciente, Paciente):
            raise TypeError("Debe ingresar un paciente válido.")

        if self.codigo_existe(paciente.codigo):
            return False

        self._pacientes.append(paciente)
        return True

    # Agregar medico
    def agregar_medico(self, medico):
        if not isinstance(medico, Medico):
            raise TypeError("Debe ingresar un médico válido.")

        if self.codigo_existe(medico.codigo):
            return False

        self._medicos.append(medico)
        return True

    # Agregar cita
    def agregar_cita(self, cita):
        if not isinstance(cita, Cita):
            raise TypeError("Debe ingresar una cita válida.")

        if self.codigo_existe(cita.codigo):
            return False

        if cita.paciente not in self._pacientes:
            return False

        if cita.medico not in self._medicos:
            return False

        self._citas.append(cita)
        return True

    # Buscar por codigo
    def buscar_por_codigo(self, codigo):
        if not isinstance(codigo, str):
            return None

        for coleccion in (
            self._pacientes,
            self._medicos,
            self._citas,
            self._historial
        ):
            for elemento in coleccion:
                if elemento.codigo == codigo:
                    return elemento

        return None

    # Filtrar citas por paciente usando filter
    def filtrar_citas_por_paciente(self, codigo_paciente):
        return list(filter(
            lambda cita: cita.paciente.codigo == codigo_paciente,
            self._citas
        ))

    # Buscar medicos por especialidad usando filter
    def buscar_por_especialidad(self, especialidad):
        return list(filter(
            lambda medico: medico.especialidad.lower() == especialidad.strip().lower(),
            self._medicos
        ))

    # Registrar atencion
    def registrar_atencion(self, atencion):
        if not isinstance(atencion, Atencion):
            raise TypeError("Debe ingresar una atención válida.")

        if atencion.cita not in self._citas:
            return False

        if self.codigo_existe(atencion.codigo):
            return False

        self._historial.append(atencion)
        return True

    # Filtrar atenciones por paciente usando filter
    def filtrar_atenciones_por_paciente(self, codigo_paciente):
        return list(filter(
            lambda atencion: atencion.cita.paciente.codigo == codigo_paciente,
            self._historial
        ))

    # Obtener resumenes de pacientes usando map
    def obtener_resumenes_pacientes(self):
        return list(map(
            lambda paciente: paciente.resumen(),
            self._pacientes
        ))

    # Contar citas usando reduce
    def contar_citas(self):
        return reduce(
            lambda total, cita: total + 1,
            self._citas,
            0
        )

    # Mostrar historial
    def mostrar_historial(self):
        for atencion in self._historial:
            print(atencion.resumen())

    # Mostrar citas
    def mostrar_citas(self):
        for cita in self._citas:
            print(cita.resumen())

    # Mostrar medicos
    def mostrar_medicos(self):
        for medico in self._medicos:
            print(medico.resumen())
