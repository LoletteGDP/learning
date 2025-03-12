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
def agregar_tarea(tareas, descripcion, importancia):
    bucle = 1
    while (bucle == 1):
        if importancia == "1":
            importancia = "alta"
            bucle = 0
        elif importancia == "2":
            importancia = "media"
            bucle = 0
        elif importancia == "3":
            importancia = "baja"
            bucle = 0
        else:
            print("⚠️ Opción no válida, intenta de nuevo.")
            print("1. alta")
            print("2. media")
            print("3. baja")
            importancia = input("\nIngrese nivel de importancia:")            
    nueva_tarea = {
        "id": len(tareas) + 1,  # ID autoincremental
        "descripcion": descripcion,
        "prioridad": importancia,
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
    
    # Crear listas para cada nivel de prioridad
    tareas_alta = []
    tareas_media = []
    tareas_baja = []

    # Clasificar tareas según su prioridad
    for tarea in tareas:
        prioridad = tarea.get("prioridad", "baja").strip().lower()  # Asume "baja" si no tiene prioridad
        
        # Calcular el tiempo restante si tiene fecha límite
        fecha_limite = tarea.get("fecha_limite", "Sin fecha")
        tiempo = tiempo_restante(tarea) if fecha_limite != "Sin fecha" else "N/A"

        estado = "✔️" if tarea["completada"] else "❌"
        tarea_info = f"{tarea['id']}. {tarea['descripcion']} [{estado}]\n - Fecha límite: {fecha_limite} - ⏳ Tiempo restante: {tiempo}"

        if prioridad == "alta":
            tareas_alta.append(tarea_info)
        elif prioridad == "media":
            tareas_media.append(tarea_info)
        else:
            tareas_baja.append(tarea_info)

    # Mostrar tareas organizadas
    if tareas_alta:
        print("\n🔥 Tareas de Alta Prioridad:")
        for tarea in tareas_alta:
            print(tarea)

    if tareas_media:
        print("\n⚖️ Tareas de Prioridad Media:")
        for tarea in tareas_media:
            print(tarea)

    if tareas_baja:
        print("\n🟢 Tareas de Baja Prioridad:")
        for tarea in tareas_baja:
            print(tarea)

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
    return "Sin fecha límite"

# Marcar  desmarcar tareas
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
            print("1. alta")
            print("2. media")
            print("3. baja")
            importancia = input("\nIngrese nivel de importancia:")
            agregar_tarea(tareas, descripcion, importancia)

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
