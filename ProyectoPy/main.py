def main():
    class Personaje:

        def __init__(self, nombre, fuerza, inteligencia, movilidad, vida, resistencia):
            self.nombre = nombre
            self.fuerza = fuerza
            self.inteligencia = inteligencia
            self.movilidad = movilidad
            self.vida = vida
            self.resistencia = resistencia
            self.turno = False

        def getAtributos(self):
            print("\nnombre:", self.nombre)
            print("vida:", self.vida)
            print("fuerza:", self.fuerza)
            print("inteligencia:", self.inteligencia)
            print("movilidad:", self.movilidad)
            print("resistencia:", self.resistencia)

        def setAumLvl(self, fuerza, inteligencia, resistencia):
            self.fuerza = self.fuerza + fuerza
            self.inteligencia = self.inteligencia + inteligencia
            self.resistencia = self.resistencia + resistencia

        def esta_vivo(self,):
            return self.vida > 0 
        
        def muerto(self):
            if self.vida < 0:
                print(f"{self.nombre} a caido") 
            return True
        
        def golpe(self, enemigo):
            return self.fuerza - enemigo.resistencia

        def atacar(self, enemigo):
            daño = self.golpe(enemigo)
            enemigo.vida = enemigo.vida - daño
            if enemigo.esta_vivo():
                print(f"\n{self.nombre} a realizado {daño} de daño a {enemigo.nombre}\nDejandole a {enemigo.vida} ps")
            else:
                print(f"\n{self.nombre} a realizado {daño} de daño a {enemigo.nombre}")
                enemigo.muerto()

class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Guerrero(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa

class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre,":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre,":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

#mi_personaje = personaje("Lolette", 10, 11, 12, 10, 14)

#enemigo = personaje("Luz", 10, 11, 12, 15, 7)

#mi_personaje.getAtributos()
#enemigo.getAtributos()
#mi_personaje.atacar(enemigo)
#mi_personaje.setAumLvl(10, 5, 5)
#mi_personaje.atacar(enemigo)


personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()      

combate(personaje_1, personaje_2)


 
if __name__ == "__main__":
    main()
