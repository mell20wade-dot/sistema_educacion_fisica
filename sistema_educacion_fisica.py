"""
Sistema de Gestión de Educación Física Estudiantil
----------------------------------------------------
Proyecto en equipo (3 integrantes). Cada bloque de código
está marcado con el nombre de la función y el integrante
responsable de esa parte.

Estructura de datos: lista de diccionarios, donde cada
diccionario representa un estudiante.
"""


# ======================================================
# BLOQUE 1 - Función: mostrar_menu()
# Responsable: [MELL BRYAN CENTONO]
# ======================================================
def mostrar_menu():
    """Muestra las opciones disponibles del programa."""
    print("\n===== SISTEMA DE EDUCACIÓN FÍSICA =====")
    print("1. Registrar estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante y evaluar condición física")
    print("4. Eliminar estudiante")
    print("5. Salir")
    print("========================================")


# ======================================================
# BLOQUE 2 - Función: registrar_estudiante()
# Responsable: [SUSANA MORENO CORDOBA]
# ======================================================
def registrar_estudiante(estudiantes):
    """Pide los datos de un estudiante por teclado y lo agrega
    a la lista."""
    print("\n--- Registrar nuevo estudiante ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    grado = input("Grado/Grupo: ")
    pechadas = int(input("Cantidad de pechadas realizadas: "))
    abdominales = int(input("Cantidad de abdominales realizadas: "))
    salto = float(input("Salto de longitud (metros): "))
    tiempo_50m = float(input("Tiempo en carrera de 50m (segundos): "))

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "grado": grado,
        "pechadas": pechadas,
        "abdominales": abdominales,
        "salto": salto,
        "tiempo_50m": tiempo_50m,
    }
    estudiantes.append(estudiante)
    print(f"Estudiante '{nombre}' registrado con éxito.")

# ======================================================
# BLOQUE 3 - Función: listar_estudiantes()
# Responsable: [SUSANA MORENO CORDOBA]
# ======================================================
def listar_estudiantes(estudiantes):
    """Muestra en pantalla el nombre y grado de todos los
    estudiantes registrados."""
    print("\n--- Lista de estudiantes ---")
    if not estudiantes:
        print("No hay estudiantes ocupa cerebro agrega estudiantes despues pide lista.")
        return

    for i, est in enumerate(estudiantes, start=1):
        print(f"{i}. {est['nombre']} - Grado: {est['grado']}")


# ======================================================
# BLOQUE 4 - Función: buscar_estudiante()
# Responsable: [SUSANA MORENO CORDOBA]
# ======================================================
def buscar_estudiante(estudiantes, nombre):
    """Busca un estudiante por nombre dentro de la lista y
    devuelve sus datos, o None si no existe."""
    for est in estudiantes:
        if est["nombre"].lower() == nombre.lower():
            return est
    return None



# ======================================================
# BLOQUE 5 - Función: evaluar_condicion_fisica()
# Responsable: [GESLER MARTIN CALDERON]
# ======================================================
def evaluar_condicion_fisica(estudiante):
    """Calcula el nivel de condición física de un estudiante
    según 4 criterios: flexiones, abdominales, salto y tiempo."""
    puntos = 0
    if estudiante["pechadas"] >= 20:
        puntos += 1
    if estudiante["abdominales"] >= 25:
        puntos += 1
    if estudiante["salto"] >= 1.5:
        puntos += 1
    if estudiante["tiempo_50m"] <= 9:
        puntos += 1

    if puntos == 4:
        return "Excelente"
    elif puntos == 3:
        return "Bueno"
    elif puntos == 2:
        return "Regular"
    else:
        return "Necesita mejorar"


# ======================================================
# BLOQUE 6 - Función: eliminar_estudiante()
# Responsable: [GESLER MARTIN CALDERON]
# ======================================================
def eliminar_estudiante(estudiantes, nombre):
    """Elimina un estudiante de la lista si existe. Devuelve
    True si se eliminó, False si no se encontró."""
    estudiante = buscar_estudiante(estudiantes, nombre)
    if estudiante:
        estudiantes.remove(estudiante)
        return True
    return False


# ======================================================
# BLOQUE 7 - Función: main()
# Responsable: [SE ARMO ENTRE LOS 3, conecta todos los bloques]
# ======================================================
def main():
    """Función principal: contiene el bucle del menú y conecta
    todas las demás funciones."""
    estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        # --- Opción 1: llama al BLOQUE 2 ---
        if opcion == "1":
            registrar_estudiante(estudiantes)

        # --- Opción 2: llama al BLOQUE 3 ---
        elif opcion == "2":
            listar_estudiantes(estudiantes)

        # --- Opción 3: llama al BLOQUE 4 y BLOQUE 5 ---
        elif opcion == "3":
            nombre = input("Nombre del estudiante a buscar: ")
            estudiante = buscar_estudiante(estudiantes, nombre)
            if estudiante:
                nivel = evaluar_condicion_fisica(estudiante)
                print(f"\n{estudiante['nombre']} - Condición física: {nivel}")
            else:
                print("Estudiante no encontrado.")

        # --- Opción 4: llama al BLOQUE 6 ---
        elif opcion == "4":
            nombre = input("Nombre del estudiante a eliminar: ")
            if eliminar_estudiante(estudiantes, nombre):
                print("Estudiante eliminado con éxito.")
            else:
                print("Estudiante no encontrado.")

        # --- Opción 5: termina el programa ---
        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
