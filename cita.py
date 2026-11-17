
from datetime import datetime
from paciente import Paciente
from medico import Medico


class Cita:
    def __init__(self, codigo, paciente, medico, fecha):
        self.codigo = codigo
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha

    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico

    @property
    def fecha(self):
        return self._fecha

    # Setters con validaciones
    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El código de la cita no puede estar vacío.")
        self._codigo = valor.strip()

    @paciente.setter
    def paciente(self, valor):
        if not isinstance(valor, Paciente):
            raise TypeError("Debe ingresar un paciente válido.")
        self._paciente = valor

    @medico.setter
    def medico(self, valor):
        if not isinstance(valor, Medico):
            raise TypeError("Debe ingresar un médico válido.")
        self._medico = valor

    @fecha.setter
    def fecha(self, valor):
        if not isinstance(valor, str):
            raise TypeError("La fecha debe ser un texto.")

        try:
            datetime.strptime(valor, "%d/%m/%Y")
        except ValueError:
            raise ValueError("La fecha debe tener el formato DD/MM/AAAA.")

        self._fecha = valor

    def resumen(self):
        return (
            f"{self._codigo} - {self._paciente.nombre} "
            f"con el Dr. {self._medico.nombre} el {self._fecha}"
        )
