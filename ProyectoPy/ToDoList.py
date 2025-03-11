import json
from datetime import datetime

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

# Agregar tarea
def agregar_tarea(tareas, descripcion):
    nueva_tarea = {
        "id": len(tareas) + 1,  # ID autoincremental
        "descripcion": descripcion,
        "completada": False,
        "fecha_limite": None  # Inicialmente sin fecha límite
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print("✅ Tarea agregada con éxito.")

# Listar tareas
def listar_tareas(tareas):
    if not tareas:
        print("📭 No hay tareas registradas.")
        return
    
    print("\n📋 Lista de tareas:")
    for tarea in tareas:
        estado = "✔️" if tarea["completada"] else "❌"
        fecha_limite = tarea.get("fecha_limite", "Sin fecha")  # Evita errores
        
        tiempo = tiempo_restante(tarea) if fecha_limite != "Sin fecha" else "N/A"
        print(f"{tarea['id']}. {tarea['descripcion']} [{estado}] - Fecha límite: {fecha_limite} - ⏳ {tiempo}")

# Marcar o desmarcar tareas
def marcar_tarea(tareas):
    listar_tareas(tareas)
    id_select = input("\nIngrese ID de la tarea a marcar/desmarcar: ")
    
    try:
        id_select = int(id_select)
        for tarea in tareas:
            if tarea['id'] == id_select:
                tarea["completada"] = not tarea["completada"]
                guardar_tareas(tareas)
                estado = "✔️" if tarea["completada"] else "❌"
                print(f"[{estado}] Tarea '{tarea['descripcion']}' actualizada.")
                return
        print("⚠️ No se encontró una tarea con ese ID.")
    except ValueError:
        print("⚠️ Ingresa un número válido.")

# Eliminar tarea
def eliminar_tareas(tareas):
    listar_tareas(tareas)
    id_select = input("\nIngrese ID de la tarea a eliminar: ")
    
    try:
        id_select = int(id_select)
        tareas[:] = [tarea for tarea in tareas if tarea['id'] != id_select]  # Filtrar la tarea eliminada
        correcion_IDs(tareas)
        guardar_tareas(tareas)
        print("🗑 Tarea eliminada con éxito.")
    except ValueError:
        print("⚠️ Ingresa un número válido.")

# Reasignar IDs
def correcion_IDs(tareas):
    for i, tarea in enumerate(tareas, start=1):
        tarea["id"] = i
    guardar_tareas(tareas)

# Asignar fecha límite a una tarea
def limitar_fecha(tareas):
    listar_tareas(tareas)
    id_select = input("\nIngrese el ID de la tarea para establecer la fecha límite: ")
    
    try:
        id_select = int(id_select)
        
        for tarea in tareas:
            if tarea['id'] == id_select:
                fecha_texto = input("Ingrese la fecha límite (ejemplo: '25-12-2024 09:30'): ")
                fecha_limit = datetime.strptime(fecha_texto, "%d-%m-%Y %H:%M")
                
                # Guardar la fecha límite en la tarea
                tarea["fecha_limite"] = fecha_limit.strftime("%d-%m-%Y %H:%M")
                guardar_tareas(tareas)

                print(f"✅ Fecha límite establecida: {tarea['fecha_limite']}")                                
                return
            
        print("⚠️ No se encontró una tarea con ese ID.")
    
    except ValueError:
        print("⚠️ Ingresa un formato de fecha válido.")

# Calcular tiempo restante de una tarea
def tiempo_restante(tarea):
    fecha_texto = tarea.get("fecha_limite")
    if fecha_texto:
        try:
            fecha_obj = datetime.strptime(fecha_texto, "%d-%m-%Y %H:%M")
            tiempo_rest = fecha_obj - datetime.now()

            if tiempo_rest.total_seconds() > 0:
                return f"{tiempo_rest.days} días, {tiempo_rest.seconds // 3600} horas"
            else:
                return "⏳ Vencida"
        except ValueError:
            return "⚠️ Fecha incorrecta"
    return "N/A"

# Función principal del menú
def main():
    tareas = cargar_tareas()

    while True:
        print("\nGestor de Tareas - Menú")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea")
        print("4. Eliminar tarea")
        print("5. Establecer fecha límite")
        print("6. Salir")

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
            limitar_fecha(tareas)

        elif opcion == "6":
            print("👋 Saliendo del gestor de tareas...")
            break

        else:
            print("⚠️ Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
