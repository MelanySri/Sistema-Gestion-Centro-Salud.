
from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion
from clinica import Clinica


clinica = Clinica()


# Registrar paciente
def registrar_paciente():
    print("\n--- REGISTRAR PACIENTE ---")

    try:
        codigo = input("Ingrese código: ")
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))

        paciente = Paciente(codigo, nombre, edad)

        if clinica.agregar_paciente(paciente):
            print("\nPaciente registrado correctamente.")
            print("Resumen:", paciente.resumen())
        else:
            print("No se pudo registrar. Verifique el código.")

    except (ValueError, TypeError) as error:
        print("Error:", error)


# Registrar médico
def registrar_medico():
    print("\n--- REGISTRAR MÉDICO ---")

    try:
        codigo = input("Ingrese código: ")
        nombre = input("Ingrese nombre: ")
        especialidad = input("Ingrese especialidad: ")

        medico = Medico(codigo, nombre, especialidad)

        if clinica.agregar_medico(medico):
            print("\nMédico registrado correctamente.")
            print("Resumen:", medico.resumen())
        else:
            print("No se pudo registrar. Verifique el código.")

    except (ValueError, TypeError) as error:
        print("Error:", error)


# Registrar cita
def registrar_cita():
    print("\n--- REGISTRAR CITA ---")

    try:
        codigo = input("Ingrese código de la cita: ")
        codigo_paciente = input("Ingrese código del paciente: ")
        codigo_medico = input("Ingrese código del médico: ")
        fecha = input("Ingrese fecha (DD/MM/AAAA): ")

        paciente = clinica.buscar_por_codigo(codigo_paciente)
        medico = clinica.buscar_por_codigo(codigo_medico)

        if not isinstance(paciente, Paciente):
            print("No se encontró el paciente.")
            return

        if not isinstance(medico, Medico):
            print("No se encontró el médico.")
            return

        cita = Cita(codigo, paciente, medico, fecha)

        if clinica.agregar_cita(cita):
            print("\nCita registrada correctamente.")
            print("Resumen:", cita.resumen())
            print("Total de citas registradas:", clinica.contar_citas())
        else:
            print("No se pudo registrar la cita. Verifique los datos.")

    except (ValueError, TypeError) as error:
        print("Error:", error)


# Buscar por código
def buscar_codigo():
    print("\n--- BUSCAR POR CÓDIGO ---")

    codigo = input("Ingrese el código que desea buscar: ")
    encontrado = clinica.buscar_por_codigo(codigo)

    if encontrado is not None:
        print("\nRegistro encontrado:")
        print(encontrado.resumen())
    else:
        print("No se encontró ningún registro.")


# Registrar atención médica
def registrar_atencion():
    print("\n--- REGISTRAR ATENCIÓN MÉDICA ---")

    try:
        codigo = input("Ingrese código de atención: ")
        codigo_cita = input("Ingrese código de la cita: ")

        cita = clinica.buscar_por_codigo(codigo_cita)

        if not isinstance(cita, Cita):
            print("No se encontró la cita.")
            return

        diagnostico = input("Ingrese diagnóstico ficticio: ")
        tratamiento = input("Ingrese tratamiento ficticio: ")

        atencion = Atencion(codigo, cita, diagnostico, tratamiento)

        if clinica.registrar_atencion(atencion):
            print("\nAtención registrada correctamente.")
            print("Resumen:", atencion.resumen())
        else:
            print("No se pudo registrar la atención.")

    except (ValueError, TypeError) as error:
        print("Error:", error)


# Buscar médico por especialidad
def buscar_especialidad():
    print("\n--- BUSCAR POR ESPECIALIDAD ---")

    especialidad = input("Ingrese la especialidad: ")
    medicos = clinica.buscar_por_especialidad(especialidad)

    if medicos:
        print("\nMédicos encontrados:")

        for medico in medicos:
            print(medico.resumen())
    else:
        print("No se encontraron médicos con esa especialidad.")


# Menú principal
def menu():
    while True:
        print("\n======================================")
        print(" SISTEMA DE GESTIÓN DEL CENTRO DE SALUD")
        print("======================================")
        print("1. Registrar paciente")
        print("2. Registrar médico")
        print("3. Registrar cita")
        print("4. Buscar por código")
        print("5. Registrar atención médica")
        print("6. Buscar médico por especialidad")
        print("7. Salir")
        print("======================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            registrar_medico()
        elif opcion == "3":
            registrar_cita()
        elif opcion == "4":
            buscar_codigo()
        elif opcion == "5":
            registrar_atencion()
        elif opcion == "6":
            buscar_especialidad()
        elif opcion == "7":
            print("\nGracias por utilizar el sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
