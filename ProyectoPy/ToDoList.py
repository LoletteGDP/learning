import json

# Archivo donde se guardarán las tareas
ARCHIVO_TAREAS = "tareas.json"

# Cargar tareas desde JSON
def cargar_tareas():
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):  
        guardar_tareas([])  # Crea el archivo si no existe
        return []

# Guardar tareas en JSON
def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4)

# FUncion Agregar tareas
def agregar_tarea(tareas, descripcion):
    nueva_tarea = {
        "id": len(tareas) + 1,  # ID autoincremental
        "descripcion": descripcion,
        "completada": False
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print("✅ Tarea agregada con éxito.")

# Funcion Listar 
def listar_tareas(tareas):
    if not tareas:
        print("📭 No hay tareas registradas.")
        return
    print("\n📋 Lista de tareas:")
    for tarea in tareas:
        estado = "✔️" if tarea["completada"] else "❌"
        print(f"{tarea['id']}. {tarea['descripcion']} [{estado}]")

# Marcar Tarea o desmarcar  
def marcar_tarea(tareas):
    listar_tareas(tareas)
    id_select = input("\ningrese id de la tarea a marcar: ")
    try:
        id_select = int(id_select)  # Convertir a entero
        for tarea in tareas:
            if tarea['id'] == id_select:
                tarea["completada"] = not tarea["completada"]
                guardar_tareas(tareas)  # Guardar cambios en el archivo
                estado = "✔️" if tarea["completada"] else "❌"
                print(f"[{estado}] Tarea '{tarea['descripcion']}' marcada.")
                return
        print("⚠️ No se encontró una tarea con ese ID.")
    except ValueError:
        print("⚠️ Ingresa un número válido.")


def eliminar_tareas(tareas):
    listar_tareas(tareas)
    id_select = input("\ningrese id de la tarea a eliminar: ")
    try:
        id_select = int(id_select)  # Convertir a entero
        for tarea in tareas:
            if tarea['id'] == id_select:
                tareas.remove(tarea)
                guardar_tareas(tareas) # Guardar cambios en el archivo
                correcion_IDs(tareas)  
                print(f"Tarea '{tarea['descripcion']}' eliminada.")
                return
        print("⚠️ No se encontró una tarea con ese ID.")
    except ValueError:
        print("⚠️ Ingresa un número válido.")

def correcion_IDs(tareas):
    # Reasignar IDs en orden
    for i, tarea in enumerate(tareas, start=1):
        tarea["id"] = i
    guardar_tareas(tareas)  # Guardar cambios en el archivo 

# Función principal del menú
def main():
    tareas = cargar_tareas()

    while True:
        print("\nGestor de Tareas - Menú")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar Tareas")
        print("4. Eliminar Tareas")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            descripcion = input("Describe la nueva tarea: ")
            agregar_tarea(tareas, descripcion)
        elif opcion == "2":
            listar_tareas(tareas)

        elif opcion == "3":
            marcar_tarea(tareas)

        elif opcion == "4":
            eliminar_tareas(tareas)


        elif opcion == "5":
            print("👋 Saliendo del gestor de tareas...")
            break
        else:
            print("⚠️ Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()


