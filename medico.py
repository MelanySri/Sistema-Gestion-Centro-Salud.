
class Medico:
    def __init__(self, codigo, nombre, especialidad):
        self.codigo = codigo
        self.nombre = nombre
        self.especialidad = especialidad

    # Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def especialidad(self):
        return self._especialidad

    # Setters
    @codigo.setter
    def codigo(self, valor):
        if not valor:
            raise ValueError("El código es obligatorio.")
        self._codigo = valor

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre es obligatorio.")
        self._nombre = valor

    @especialidad.setter
    def especialidad(self, valor):
        if not valor:
            raise ValueError("La especialidad es obligatoria.")
        self._especialidad = valor

    def resumen(self):
        return f"{self._codigo} - {self._nombre} - {self._especialidad}"