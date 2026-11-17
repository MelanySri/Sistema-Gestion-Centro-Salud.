
from cita import Cita


class Atencion:
    def __init__(self, codigo, cita, diagnostico, tratamiento):
        self.codigo = codigo
        self.cita = cita
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def cita(self):
        return self._cita

    @property
    def diagnostico(self):
        return self._diagnostico

    @property
    def tratamiento(self):
        return self._tratamiento

    # Setters con validaciones
    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El código de atención no puede estar vacío.")
        self._codigo = valor.strip()

    @cita.setter
    def cita(self, valor):
        if not isinstance(valor, Cita):
            raise TypeError("Debe ingresar una cita válida.")
        self._cita = valor

    @diagnostico.setter
    def diagnostico(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El diagnóstico no puede estar vacío.")
        self._diagnostico = valor.strip()

    @tratamiento.setter
    def tratamiento(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El tratamiento no puede estar vacío.")
        self._tratamiento = valor.strip()

    def resumen(self):
        return (
            f"{self._codigo} - {self._cita.paciente.nombre} - "
            f"{self._diagnostico} - {self._tratamiento}"
        )