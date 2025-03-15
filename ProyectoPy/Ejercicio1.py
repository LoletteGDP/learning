
def main():
    personajes_principales = [
    ("Astarion", 239, "Rogue", "Elf", 3, True),
    ("Shadowheart", 40, "Cleric", "Half-Elf", 5, True),
    ("Wyll", 25, "Warlock", "Human", 2, False),
    ("Gale", 35, "Wizard", "Human", 5, True),
    ("Karlach", 32, "Barbarian", "Tiefling", 6, False),
    ("Lae'zel", 20, "Fighter", "Githyanki", 4, True),
    ("Jaheira", 150, "Druid", "Half-Elf", 6, False),
    ("Halsin", 350, "Druid", "Elf", 7, False),
    ("Minsc", 130, "Ranger", "Human", 5, False),
    ("Minthara", 250, "Paladin", "Drow", 8, False),
    ("Dark Urge", 30, "Sorcerer", "Dragonborn", 1, False)
]
    # 1
    def calcular_PromLvl(personajes):
        totalPjs = 0
        total_Lvl = 0
        for personajes in personajes_principales:
            if personajes[5]:
                totalPjs +=1
                total_Lvl += personajes [4]
        return int(total_Lvl / totalPjs)
    
    #2
    def filtrar_equipo(personajes):
        personajes_equipo = []
        for personajes in personajes_principales: 
            if personajes[5]:
                personajes_equipo.append(personajes)
        return personajes_equipo

    #resolucion propia 3
    def obtener_clase(personajes):
        lista_clases = []
        for  personajes in personajes_principales:
            lista_clases.append(personajes[2])
            if lista_clases.count(personajes[2])> 1:
                lista_clases.remove(personajes[2])
        return lista_clases
    
    #la del video 3
    def obtener_clase2(personajes):
        lista_clases = set()
        for  personajes in personajes_principales:
            lista_clases.add(personajes[2])
        return lista_clases

    #resolucion propia 4
    def contar_razas(personajes):
        dict_razas={
        }
        lista_razas = []
        for personajes in personajes_principales:
            lista_razas.append(personajes[3])
            dict_razas[personajes[3]]=lista_razas.count(personajes[3])
        return dict_razas
    
    #la del video 4
    def contar_razas2(personajes):
        dict_razas={
        }
        for personajes in personajes_principales:
            raza = personajes[3]
            if raza in dict_razas:
               dict_razas[raza] += 1
            else:
               dict_razas[raza] = 1
        return dict_razas

    #5
    def verificar_existencia_raza(personajes, raza):
        for personajes in personajes_principales:
            if raza == personajes[3]:
                return True
        return False    

    #desaprobado 6
    def personaje_mayorLvl(personajes, clase= None):
        list_lvls = []
        for personajes in personajes_principales:
            if personajes[2] ==clase:
                list_lvls.append(personajes[4])
                if list_lvls[0] <= list_lvls[1]:
                    list_lvls.remove(0)
                if list_lvls[0] >= list_lvls[1]:
                    list_lvls.remove(1)
            elif clase == None:
                list_lvls.append(personajes[4])
                if list_lvls[0] <= list_lvls[1]:
                    list_lvls.remove(0)
                if list_lvls[0] >= list_lvls[1]:
                     list_lvls.remove(1)
            else:
                pass
        lvlmax = max(list_lvls) 
        for personajes in personajes_principales:
            if lvlmax == personajes[4]:       
                return personajes[0]
    
    # mucho mas simple desaprobe 6
    def personaje_mayorlvl(personajes, clase= None):
        maximo = 0
        nombre = None
        for personajes in personajes_principales:
            if clase == None or clase == personajes[2]:
                if personajes[4] > maximo:
                    nombre = personajes[0]
                    maximo = personajes[4]
        return nombre

    # 7
    def incrementar_nivel2(personajes, nombre_buscado):
        for personajes in personajes_principales:
            if personajes[0] == nombre_buscado:
                new_personaje = (personajes[0], 
                                 personajes[1], 
                                 personajes[2],
                                 personajes[3],
                                 personajes[4] + 1, 
                                 personajes[5])
                print(new_personaje[4])
                personajes_principales.remove(personajes)
                personajes_principales.append(new_personaje)
                return
 
    #7 mejor?
    def incrementar_nivel(personajes, nombre_buscado):
        for i in range(len(personajes)):
            if personajes[i][0] == nombre_buscado:
                personajes[i] = (personajes[i][0], 
                                 personajes[i][1], 
                                 personajes[i][2],
                                 personajes[i][3],
                                 personajes[i][4] + 1, 
                                 personajes[i][5])
                print(personajes[i][4])

    def adivina_edad(personajes, nombre_buscado):
        for personajes in personajes_principales:
            if personajes[0] == nombre_buscado:
                edad_ingresada = -1
                while edad_ingresada != personajes[1] or edad_ingresada == 0 :
                    edad_ingresada = int(input(f"introduzca la edad de {personajes[0]}:"))
                    if edad_ingresada == personajes[0]:
                        return print ("ACERTASTEEEE!!! EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                    elif edad_ingresada == 0:
                        print("interrupcion del jugador")
                        return  
                    elif edad_ingresada < personajes[1]:
                        print("La edad es mayor a la puesta")
                    else: 
                        print("La edad es menor a la puesta")
        print("personaje no reconocido")
                
    print("Hola soy main")
    print(calcular_PromLvl(personajes_principales))
    print()
    print(filtrar_equipo(personajes_principales))
    print()
    print(obtener_clase2(personajes_principales))
    print()
    print(contar_razas(personajes_principales))
    print()
    print(verificar_existencia_raza(personajes_principales, "Human"))
    print()
    print(verificar_existencia_raza(personajes_principales, "Gnome"))
    print()
    print(personaje_mayorlvl(personajes_principales))
    print()
    print(personaje_mayorlvl(personajes_principales, "Druid"))
    print()
    incrementar_nivel(personajes_principales, "Gale")
    print(personajes_principales)
    adivina_edad(personajes_principales, input("introduzca el nombre de quien adivinar la edad:"))

if __name__ == "__main__":
    main()
