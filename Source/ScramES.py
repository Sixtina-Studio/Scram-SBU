# --------------------------------------------------------------------
# SCRAM SBU PROJECT, BY SIXTINA STUDIO 2026, DEVELOPED BY MARCOKISTAN
# --------------------------------------------------------------------

"""Este proyecto fué creado con el proposito de aprender Programación Orientada a Objetos
Me ha servido personalmente, y de paso he conseguido crear un videojuego bastante
interesante, pese a que su interfaz esta basada en SHELL BASED UI.

SCRAM SBU usa parte del código de Benux 2.0 para controlar el sistema de comandos.
Funciona con un bucle while que constantemente espera un nuevo comando en cada iteración

Software by: Marco Rodríguez Acosta

"""


Dinero = 9000
DineroPrivado = 9000
Bounty = 0
DictAmigable = {}
DictEnemigos = {}
CommandLine = ""
ActualMission = ""
mision = 1
total_aviones = 0


import os
import time
import sys

class avion:
    def __init__(self, nombre, ataque, vida, alianza):
        global DictAmigable, Dinero, total_aviones
        self._nombre = nombre
        self._ataque = ataque
        self._vida = vida
        self._alianza = alianza
        Dinero -= 20
        # For now, alliances are fixed to: NATO and EAST
        if alianza == "NATO":
            DictAmigable[nombre] = self
            total_aviones += 1
        else:
            DictEnemigos[nombre] = self
    @property
    def av_nombre(self):
        return self._nombre
    @av_nombre.setter
    def av_nombre(self, nombre):
        self._nombre = nombre
    @property
    def av_ataque(self):
        return self._ataque
    @av_ataque.setter
    def av_ataque(self, ataque):
        global Dinero
        dinero_a_gastar = ataque * 10
        if dinero_a_gastar > Dinero:
            print("\nSe nos ha acabado el presupuesto!")
        else:
            Dinero = Dinero - dinero_a_gastar
            self._ataque = self._ataque + ataque
            print(f"\n{self._nombre} ahora tiene {self._ataque} Ptos. de Armamento!")
    @property
    def av_vida(self):
        return self._vida
    @av_vida.setter
    def av_vida(self, tupla):
        global Dinero
        vida = tupla[0]
        decrece = tupla[1]
        if decrece == False:
            dinero_a_gastar = vida * 10
            if dinero_a_gastar > Dinero:
                print("\nSe nos ha acabado el presupuesto!")
            else:
                Dinero = Dinero - dinero_a_gastar
                self._vida += vida
                print(f"{self._nombre} ahora tiene {self._vida} Ptos. de Fuselaje!")
        else:
            self._vida -= vida
            



    
def ScreenClearing():
    os.system('cls' if os.name == 'nt' else 'clear')

def MissionClearing(string):
    global ActualMission, counter
    ActualMission = string
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ActualMission)
    

def NewCommand():
    global CommandLine, Dinero
    CommandLine = ""
    try:
        while CommandLine == "":
            CommandLine = input(f"Presupuesto -> {Dinero}M >: ")
        Executer()
    except:
        NewCommand()

def history():
    ScreenClearing()
    print("  ______    ______   _______    ______   __       __         ______   _______   __    __ \n /      \\  /      \\ /       \\  /      \\ /  \\     /  |       /      \\ /       \\ /  |  /  |\n/$$$$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$  |$$  \\   /$$ |      /$$$$$$  |$$$$$$$  |$$ |  $$ |\n$$ \\__$$/ $$ |  $$/ $$ |__$$ |$$ |__$$ |$$$  \\ /$$$ |      $$ \\__$$/ $$ |__$$ |$$ |  $$ |\n$$      \\ $$ |      $$    $$< $$    $$ |$$$$ /$$$$  |      $$      \\ $$    $$< $$ |  $$ |\n $$$$$$  |$$ |  __  $$$$$$$  |$$$$$$$$ |$$ $$ $$/$$ |       $$$$$$  |$$$$$$$  |$$ |  $$ |\n/  \\__$$ |$$ \\__/  |$$ |  $$ |$$ |  $$ |$$ |$$$/ $$ |      /  \\__$$ |$$ |__$$ |$$ \\__$$ |\n$$    $$/ $$    $$/ $$ |  $$ |$$ |  $$ |$$ | $/  $$ |      $$    $$/ $$    $$/ $$    $$/ \n $$$$$$/   $$$$$$/  $$/   $$/ $$/   $$/ $$/      $$/        $$$$$$/  $$$$$$$/   $$$$$$/  ")
    print(f"\n\nEl 28 de febrero de 2026 y tras semanas de anticipación, Israel y EEUU dan\ncomienzo a Furia Épica.\n\nEsta operación marcaría el comienzo de otra guerra más en el Medio Oriente.\nEstados Unidos te ha nombrado jefe de operaciones en el USS Abraham Lincoln.\n\nTu trabajo es liderar la ofensiva aerea.")
    input("\nPulse Enter para continuar...")
    ScreenClearing()
    print("Un juego creado por:")
    print("\n   _____ _______   _______ _____  _   _          \n  / ____|_   _\\ \\ / /_   _|_   _|| \\ | |   /\\    \n | (___   | |  \\ V /  | |   | |  |  \\| |  /  \\   \n  \\___ \\  | |   > <   | |   | |  | . ` | / /\\ \\  \n  ____) |_| |_ / . \\  | |  _| |_ | |\\  |/ ____ \\ \n |_____/|_____/_/ \\_\\ |_| |_____||_| \\_/_/    \\_\\\n\n   _____ _______ _    _ _____ _____  ____  \n  / ____|__   __| |  | |  __ \\_   _|/ __ \\ \n | (___    | |  | |  | | |  | || | | |  | |\n  \\___ \\   | |  | |  | | |  | || | | |  | |\n  ____) |  | |  | |__| | |__| || |_| |__| |\n |_____/   |_|   \\____/|_____/_____|\\____/ \n")
    input("\nPulse Enter para continuar...")
    first_mission_tutorial()

def get_best_stat():
    global DictEnemigos
    aux_lista_nombres = []
    aux_lista_vida = []
    aux_lista_daño = []
    aux_lista_daño_sorted = []
    for nombre_av in DictEnemigos:
        aux_lista_nombres.append(nombre_av)
        aux_lista_daño.append(DictEnemigos[nombre_av].av_ataque)
        aux_lista_vida.append(DictEnemigos[nombre_av].av_vida)
    aux_lista_daño_sorted = sorted(aux_lista_daño)
    counter = 0
    for valor in aux_lista_daño:
        if valor == aux_lista_daño_sorted[-1]:
            break
        else:
            counter += 1
    return aux_lista_nombres[counter], aux_lista_daño[counter], aux_lista_vida[counter]

def reset_the_scene():
    global DictAmigable, DictEnemigos, mision, Dinero, DineroPrivado
    DictAmigable = {}
    DictEnemigos = {}
    mision = 1
    if Dinero < 9000: # to not softlock the player
        Dinero = 9000
        DineroPrivado = 9000
    mission_guider()

def ending():
    global DictAmigable, Dinero, total_aviones
    ScreenClearing()
    time.sleep(2)
    print(" /$$     /$$ /$$$$$$  /$$   /$$       /$$      /$$ /$$$$$$ /$$   /$$       /$$ /$$ /$$\n|  $$   /$$//$$__  $$| $$  | $$      | $$  /$ | $$|_  $$_/| $$$ | $$      | $$| $$| $$\n \\  $$ /$$/| $$  \\ $$| $$  | $$      | $$ /$$$| $$  | $$  | $$$$| $$      | $$| $$| $$\n  \\  $$$$/ | $$  | $$| $$  | $$      | $$/$$ $$ $$  | $$  | $$ $$ $$      | $$| $$| $$\n   \\  $$/  | $$  | $$| $$  | $$      | $$$$_  $$$$  | $$  | $$  $$$$      |__/|__/|__/\n    | $$   | $$  | $$| $$  | $$      | $$$/ \\  $$$  | $$  | $$\\  $$$                  \n    | $$   |  $$$$$$/|  $$$$$$/      | $$/   \\  $$ /$$$$$$| $$ \\  $$       /$$ /$$ /$$\n    |__/    \\______/  \\______/       |__/     \\__/|______/|__/  \\__/      |__/|__/|__/")
    time.sleep(3)
    print("\n\nMaravilloso trabajo Capitan, has cumplido tu deber perfectamente, Gloria a los Estados Unidos De America!!!")
    print(f"{Dinero}M de dolares obtenidos\n{total_aviones} aviones puestos en SCRAM")
    input("Pulse cualquier tecla para continuar...")
    ScreenClearing()
    print("\n   _____ _______   _______ _____  _   _          \n  / ____|_   _\\ \\ / /_   _|_   _|| \\ | |   /\\    \n | (___   | |  \\ V /  | |   | |  |  \\| |  /  \\   \n  \\___ \\  | |   > <   | |   | |  | . ` | / /\\ \\  \n  ____) |_| |_ / . \\  | |  _| |_ | |\\  |/ ____ \\ \n |_____/|_____/_/ \\_\\ |_| |_____||_| \\_/_/    \\_\\\n\n   _____ _______ _    _ _____ _____  ____  \n  / ____|__   __| |  | |  __ \\_   _|/ __ \\ \n | (___    | |  | |  | | |  | || | | |  | |\n  \\___ \\   | |  | |  | | |  | || | | |  | |\n  ____) |  | |  | |__| | |__| || |_| |__| |\n |_____/   |_|   \\____/|_____/_____|\\____/ \n")
    print("\n\nA game made by Marco Rodríguez Acosta\n\nSixtina Studio 2026")
    input("Pulse cualquier tecla para continuar...")
    sys.exit()

def first_mission_tutorial():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    ScreenClearing()
    print(f"\nSe han detectado 4 aviones enemigos en territorio aliado!\nRápido, tenemos que derribarlos a todos, Capitan, te pondre al día rápidamente\n\nEl dinero presupuestado por el Estado es: {Dinero}M de Dolares.\nEl dinero se utiliza para poner operativos aviones y para armarlos, mejorar su fuselaje, etc...\nNuestro radar es capaz de detectar el nº de aviones enemigos en territorio aliado, pero\nno es capaz de decirnos las estadisticas de cada uno, nuestros marineros sin embargo,\npueden darnos información del mejor avión detectado por Radar, gracias a metodos más ortodoxos...\n\nAntes de lanzar una operación, siempre puedes poner más aviones operativos, puedes quitarlos y mejorarlos\n\nEscribe /h para conocer los comandos en cualquier momento...\n")
    input("Pulse Enter para continuar...")
    counter = 0
    # creating the enemies
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("F-14", 25, 100, "EAST")
    aux_en2 = avion("F4", 15, 70, "EAST")
    aux_en3 = avion("F5", 15, 60, "EAST")
    aux_en4 = avion("MIG-29", 15, 40, "EAST")
    #aux_en5 = avion("F-14", 99999, 99999, "NATO") #debug
    Dinero = DineroPrivado # tal y como lo hice, es solo una clase, avion, que cuesta dinero al jugador aunque sea enemigo asi que, conviene siempre guardar el dinero del jugador.
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 3000
    story1 = f"Aviones Detectados -> {counter}\n\n----------------------------  ESTADISTICAS AVIÓN CON MAYOR PTOS.ARMAMENTO  ----------------------------\n{bestname}.........Ptos. de Armamento: {beststat}.........Ptos. de Fuselaje: {besthealth}\nResto de Aviones: Desconocido.....................................\n\nPrepara la operación, una vez la operación empiece no podrás modificar los aviones\nEscribe /h para conocer los comandos\n\n"
    MissionClearing(story1)

def second_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    # creating the enemies
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("F5", 15, 50, "EAST")
    aux_en2 = avion("MIG-29", 6, 70, "EAST")
    aux_en3 = avion("SU-24", 7, 60, "EAST")
    aux_en4 = avion("MIG-29-2", 8, 40, "EAST")
    aux_en5 = avion("MIG-29-3", 9, 40, "EAST")
    aux_en6 = avion("MIG-29-4", 12, 80, "EAST")
    Dinero = DineroPrivado # tal y como lo hice, es solo una clase, avion, que cuesta dinero al jugador aunque sea enemigo asi que, conviene siempre guardar el dinero del jugador.
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 4000
    story2 = f"Capitan, nuestro radar ha pillado el inicio de una operación enemiga, hacemos scram?\nAviones Detectados -> {counter}\n\n----------------------------  ESTADISTICAS AVIÓN CON MAYOR PTOS.ARMAMENTO  ----------------------------\n{bestname}.........Ptos. de Armamento: {beststat}.........Ptos. de Fuselaje: {besthealth}\nResto de Aviones: Desconocido.....................................\n\nPrepara la operación, una vez la operación empiece no podrás modificar los aviones\nEscribe /h para conocer los comandos\n\n"
    MissionClearing(story2)

def third_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    # creating the enemies
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("F5", 12, 50, "EAST")
    aux_en2 = avion("MIG-29", 4, 70, "EAST")
    aux_en3 = avion("SU-24", 7, 60, "EAST")
    aux_en4 = avion("MIG-29-2", 28, 40, "EAST")
    aux_en5 = avion("MIG-29-3", 11, 40, "EAST")
    aux_en6 = avion("MIG-29-4", 12, 80, "EAST")
    aux_en7 = avion("F14", 12, 100, "EAST")
    Dinero = DineroPrivado # tal y como lo hice, es solo una clase, avion, que cuesta dinero al jugador aunque sea enemigo asi que, conviene siempre guardar el dinero del jugador.
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 5000
    story3 = f"El golfo persico no nos da descanso,Iran ha mandado unos cuantos aviones, hacemos scram?\nAviones Detectados -> {counter}\n\n----------------------------  ESTADISTICAS AVIÓN CON MAYOR PTOS.ARMAMENTO  ----------------------------\n{bestname}.........Ptos. de Armamento: {beststat}.........Ptos. de Fuselaje: {besthealth}\nResto de Aviones: Desconocido.....................................\n\nPrepara la operación, una vez la operación empiece no podrás modificar los aviones\nEscribe /h para conocer los comandos\n\n"
    MissionClearing(story3)
    
def fourth_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    # creating the enemies
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("HESA-KOWSAR", 50, 70, "EAST")
    aux_en2 = avion("F14", 20, 100, "EAST")
    Dinero = DineroPrivado # tal y como lo hice, es solo una clase, avion, que cuesta dinero al jugador aunque sea enemigo asi que, conviene siempre guardar el dinero del jugador.
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 2000
    story4 = f"Capitan, hemos detectado dos aviones en nuestro radar, nos informan que presentan una amenaza real\npese a que solo sean dos aviones.\nAviones Detectados -> {counter}\n\n----------------------------  ESTADISTICAS AVIÓN CON MAYOR PTOS.ARMAMENTO  ----------------------------\n{bestname}.........Ptos. de Armamento: {beststat}.........Ptos. de Fuselaje: {besthealth}\nResto de Aviones: Desconocido.....................................\n\nPrepara la operación, una vez la operación empiece no podrás modificar los aviones\nEscribe /h para conocer los comandos\n\n"
    MissionClearing(story4)

def fifth_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    # creating the enemies
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("F5", 7, 20, "EAST")
    aux_en2 = avion("F7", 7, 20, "EAST")
    aux_en3 = avion("SU-24", 7, 20, "EAST")
    aux_en4 = avion("MIG-29-2", 7, 20, "EAST")
    aux_en5 = avion("MIG-29-3", 7, 20, "EAST")
    aux_en6 = avion("MIG-29-4", 7, 20, "EAST")
    aux_en7 = avion("F14", 7, 20, "EAST")
    aux_en8 = avion("MIG-27", 7, 20, "EAST")
    aux_en9 = avion("MIG-29-5", 7, 20, "EAST")
    aux_en10 = avion("F14-2", 7, 20, "EAST")
    Dinero = DineroPrivado # tal y como lo hice, es solo una clase, avion, que cuesta dinero al jugador aunque sea enemigo asi que, conviene siempre guardar el dinero del jugador.
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 4000
    story5 = f"CAPITAN! Se ha detectado un gran numero de aviones enemigos en nuestra direccion, SCRAM SCRAM SCRAM\nAviones Detectados -> {counter}\n\n----------------------------  ESTADISTICAS AVIÓN CON MAYOR PTOS.ARMAMENTO  ----------------------------\n{bestname}.........Ptos. de Armamento: {beststat}.........Ptos. de Fuselaje: {besthealth}\nResto de Aviones: Desconocido.....................................\n\nPrepara la operación, una vez la operación empiece no podrás modificar los aviones\nEscribe /h para conocer los comandos\n\n"
    MissionClearing(story5)

def sixth_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    # creating the enemies
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("F5", 13, 20, "EAST")
    aux_en2 = avion("F7", 24, 20, "EAST")
    aux_en3 = avion("SU-24", 23, 20, "EAST")
    aux_en4 = avion("MIG-29-2", 7, 20, "EAST")
    aux_en5 = avion("MIG-29-3", 13, 20, "EAST")
    aux_en6 = avion("MIG-29-4", 7, 20, "EAST")
    aux_en7 = avion("F14", 19, 20, "EAST")
    aux_en8 = avion("MIG-27", 7, 20, "EAST")
    aux_en9 = avion("MIG-29-5", 7, 20, "EAST")
    aux_en10 = avion("F14-2", 14, 20, "EAST")
    aux_en11 = avion("F14-3", 7, 20, "EAST")
    aux_en12 = avion("MIG-27-2", 7, 20, "EAST")
    aux_en13 = avion("MIG-29-6", 10, 20, "EAST")
    aux_en14 = avion("F14-4", 25, 20, "EAST")
    Dinero = DineroPrivado # tal y como lo hice, es solo una clase, avion, que cuesta dinero al jugador aunque sea enemigo asi que, conviene siempre guardar el dinero del jugador.
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 7000
    story6 = f"Se aproximan aviones a nuestras bases militares, DEBEMOS derribarlos!\nAviones Detectados -> {counter}\n\n----------------------------  ESTADISTICAS AVIÓN CON MAYOR PTOS.ARMAMENTO  ----------------------------\n{bestname}.........Ptos. de Armamento: {beststat}.........Ptos. de Fuselaje: {besthealth}\nResto de Aviones: Desconocido.....................................\n\nPrepara la operación, una vez la operación empiece no podrás modificar los aviones\nEscribe /h para conocer los comandos\n\n"
    MissionClearing(story6)

def seven_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    # creating the enemies
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("F5", 13, 15, "EAST")
    aux_en2 = avion("F7", 24, 20, "EAST")
    aux_en3 = avion("SU-24", 23, 20, "EAST")
    aux_en4 = avion("MIG-29-2", 7, 20, "EAST")
    aux_en5 = avion("MIG-29-3", 13, 20, "EAST")
    aux_en6 = avion("MIG-29-4", 7, 20, "EAST")
    aux_en7 = avion("F14", 19, 20, "EAST")
    aux_en8 = avion("MIG-27", 7, 20, "EAST")
    aux_en9 = avion("MIG-29-5", 7, 15, "EAST")
    aux_en10 = avion("F14-2", 14, 20, "EAST")
    aux_en11 = avion("F14-3", 7, 20, "EAST")
    aux_en12 = avion("MIG-27-2", 7, 20, "EAST")
    aux_en13 = avion("MIG-29-6", 10, 15, "EAST")
    aux_en14 = avion("F14-4", 25, 20, "EAST")
    aux_en15 = avion("F14-5", 19, 20, "EAST")
    aux_en16 = avion("MIG-27-3", 7, 20, "EAST")
    aux_en17 = avion("MIG-29-7", 7, 20, "EAST")
    aux_en18 = avion("F14-6", 14, 15, "EAST")
    aux_en19 = avion("F14-7", 7, 20, "EAST")
    aux_en20 = avion("MIG-27-4", 7, 20, "EAST")
    aux_en21 = avion("MIG-29-8", 10, 15, "EAST")
    aux_en22 = avion("F14-8", 29, 20, "EAST")
    Dinero = DineroPrivado # tal y como lo hice, es solo una clase, avion, que cuesta dinero al jugador aunque sea enemigo asi que, conviene siempre guardar el dinero del jugador.
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 11000
    story7 = f"Parece que Iran nos considera un objetivo importante, no me extraña, hemos derribado más de 20 aviones suyos, vienen más capitan!\nAviones Detectados -> {counter}\n\n----------------------------  ESTADISTICAS AVIÓN CON MAYOR PTOS.ARMAMENTO  ----------------------------\n{bestname}.........Ptos. de Armamento: {beststat}.........Ptos. de Fuselaje: {besthealth}\nResto de Aviones: Desconocido.....................................\n\nPrepara la operación, una vez la operación empiece no podrás modificar los aviones\nEscribe /h para conocer los comandos\n\n"
    MissionClearing(story7)

def eight_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    # creating the enemies
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("DRON Shahed-136", 70, 1, "EAST")
    aux_en2 = avion("MIG-29", 4, 70, "EAST")
    aux_en3 = avion("SU-24", 7, 60, "EAST")
    aux_en4 = avion("MIG-29-2", 28, 40, "EAST")
    aux_en5 = avion("MIG-29-3", 11, 40, "EAST")
    aux_en6 = avion("MIG-29-4", 12, 80, "EAST")
    aux_en7 = avion("F14", 12, 100, "EAST")
    Dinero = DineroPrivado # tal y como lo hice, es solo una clase, avion, que cuesta dinero al jugador aunque sea enemigo asi que, conviene siempre guardar el dinero del jugador.
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 7000
    story8 = f"Capitan, me da a mi que se están quedando sin aviones, estan empezando a mandar drones!\nLos drones tienen buen ataque,pero muy pocos ptos. de fuselaje\nAviones Detectados -> {counter}\n\n----------------------------  ESTADISTICAS AVIÓN CON MAYOR PTOS.ARMAMENTO  ----------------------------\n{bestname}.........Ptos. de Armamento: {beststat}.........Ptos. de Fuselaje: {besthealth}\nResto de Aviones: Desconocido.....................................\n\nPrepara la operación, una vez la operación empiece no podrás modificar los aviones\nEscribe /h para conocer los comandos\n\n"
    MissionClearing(story8)

def nine_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    # creating the enemies
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("DRON Shahed-136", 70, 1, "EAST")
    aux_en2 = avion("DRON Shahed-131", 70, 1, "EAST")
    aux_en3 = avion("DRON Shahed-136b", 70, 1, "EAST")
    aux_en4 = avion("MIG-29-2", 28, 40, "EAST")
    aux_en5 = avion("MIG-29-3", 7, 40, "EAST")
    aux_en6 = avion("F4", 12, 80, "EAST")
    aux_en7 = avion("F14", 15, 100, "EAST")
    Dinero = DineroPrivado # tal y como lo hice, es solo una clase, avion, que cuesta dinero al jugador aunque sea enemigo asi que, conviene siempre guardar el dinero del jugador.
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 8000
    story9 = f"Se acercan más drones, son más SHAHED, scram!\nAviones Detectados -> {counter}\n\n----------------------------  ESTADISTICAS AVIÓN CON MAYOR PTOS.ARMAMENTO  ----------------------------\n{bestname}.........Ptos. de Armamento: {beststat}.........Ptos. de Fuselaje: {besthealth}\nResto de Aviones: Desconocido.....................................\n\nPrepara la operación, una vez la operación empiece no podrás modificar los aviones\nEscribe /h para conocer los comandos\n\n"
    MissionClearing(story9)

def last_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    ScreenClearing()
    time.sleep(2)
    print("Capitan...\n")
    time.sleep(2)
    print("Esta misión es diferente...")
    time.sleep(2)
    print("Tenemos que lanzar ahora nosotros un ataque, hay que prepararse como nunca\n")
    time.sleep(5)
    counter = 0
    # creating the enemies
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("F5", 13, 15, "EAST")
    aux_en2 = avion("F7", 24, 20, "EAST")
    aux_en3 = avion("SU-24", 23, 20, "EAST")
    aux_en4 = avion("MIG-29-2", 7, 20, "EAST")
    aux_en5 = avion("MIG-29-3", 13, 20, "EAST")
    aux_en6 = avion("MIG-29-4", 7, 20, "EAST")
    aux_en7 = avion("F14-1", 19, 20, "EAST")
    aux_en8 = avion("MIG-27-1", 7, 20, "EAST")
    aux_en9 = avion("MIG-29-5", 7, 15, "EAST")
    aux_en10 = avion("F14-2", 14, 20, "EAST")
    aux_en11 = avion("F14-3", 7, 20, "EAST")
    aux_en12 = avion("MIG-27-2", 7, 20, "EAST")
    aux_en13 = avion("MIG-29-6", 10, 15, "EAST")
    aux_en14 = avion("F14-4", 25, 20, "EAST")
    aux_en15 = avion("F14-5", 19, 20, "EAST")
    aux_en16 = avion("MIG-27-3", 7, 20, "EAST")
    aux_en17 = avion("MIG-29-7", 7, 20, "EAST")
    aux_en18 = avion("F14-6", 14, 15, "EAST")
    aux_en19 = avion("F14-7", 7, 20, "EAST")
    aux_en20 = avion("MIG-27-4", 7, 20, "EAST")
    aux_en21 = avion("MIG-29-8", 10, 15, "EAST")
    aux_en22 = avion("F14-8", 29, 20, "EAST")
    aux_en23 = avion("F5-B", 13, 15, "EAST")
    aux_en24 = avion("F7-B", 24, 20, "EAST")
    aux_en25 = avion("SU-24-B", 23, 20, "EAST")
    aux_en26 = avion("MIG-29-9", 7, 20, "EAST")
    aux_en27 = avion("MIG-29-10", 13, 20, "EAST")
    aux_en28 = avion("MIG-29-11", 7, 20, "EAST")
    aux_en29 = avion("F14-9", 19, 20, "EAST")
    aux_en30 = avion("MIG-27-5", 7, 20, "EAST")
    aux_en31 = avion("MIG-29-12", 7, 15, "EAST")
    aux_en32 = avion("F14-10", 14, 20, "EAST")
    aux_en33 = avion("F14-11", 7, 20, "EAST")
    aux_en34 = avion("MIG-27-6", 7, 20, "EAST")
    aux_en35 = avion("MIG-29-13", 10, 15, "EAST")
    aux_en36 = avion("F14-12", 25, 20, "EAST")
    aux_en37 = avion("F14-13", 19, 20, "EAST")
    aux_en38 = avion("MIG-27-7", 7, 20, "EAST")
    aux_en39 = avion("MIG-29-14", 7, 20, "EAST")
    aux_en40 = avion("F14-14", 14, 15, "EAST")
    aux_en41 = avion("F14-15", 7, 20, "EAST")
    aux_en42 = avion("MIG-27-8", 7, 20, "EAST")
    aux_en43 = avion("MIG-29-15", 10, 15, "EAST")
    aux_en44 = avion("F14-16", 29, 20, "EAST")
    Dinero = DineroPrivado # tal y como lo hice, es solo una clase, avion, que cuesta dinero al jugador aunque sea enemigo asi que, conviene siempre guardar el dinero del jugador.
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 5000
    story_last = f"Capitan...Esta misión es diferente...\nTenemos que lanzar ahora nosotros un ataque, hay que prepararse como nunca\n\nAviones Detectados -> {counter}\n\n----------------------------  ESTADISTICAS AVIÓN CON MAYOR PTOS.ARMAMENTO  ----------------------------\n{bestname}.........Ptos. de Armamento: {beststat}.........Ptos. de Fuselaje: {besthealth}\nResto de Aviones: Desconocido.....................................\n\nPrepara la operación, una vez la operación empiece no podrás modificar los aviones\nEscribe /h para conocer los comandos\n\n"
    MissionClearing(story_last)

def mission_guider():
    if mision == 1:
        first_mission_tutorial()
    elif mision == 2:
        second_mision()
    elif mision == 3:
        third_mision()
    elif mision == 4:
        fourth_mision()
    elif mision == 5:
        fifth_mision()
    elif mision == 6:
        sixth_mision()
    elif mision == 7:
        seven_mision()
    elif mision == 8:
        eight_mision()
    elif mision == 9:
        nine_mision()
    elif mision == 10:
        last_mision()
        

##############################################################

def Executer():
    global CommandLine, Dinero, DictAmigable, DictEnemigos, Bounty, mision, ActualMission


    # COMANDOS HELP
    
    if CommandLine == "/h":
        MissionClearing(ActualMission)
        print("PREPARACIÓN DE LA OPERACIÓN:\n---------------------\n/scramjet\nPondrás operativo un jet de combate, esta acción cuesta 20M\n\n/modificar nombre_jet\nEl nombre del jet va seguido al comando, permite modificar su FUSELAJE y ARMAMENTO\n\n/decomision nombre_jet\nEl nombre del jet va seguido al comando, permite eliminar a un jet de la operación\nse reembolsa el coste de poner el jet operativo\n\nOPERACIÓN\n---------------------\n/catapultar\nlanza los jets del portaviones y da comienzo a la operación, escribe este comando cuando estes listo\n")
    else:
        pass

    # PRE-OPERACION

    if CommandLine == "/SCRAMJET" or CommandLine == "/scramjet":
        MissionClearing(ActualMission)
        print("Si mi capitan!")
        aux_nombre = input("Dale un call-sign al avion: ")
        for av_ref in DictAmigable:
            if aux_nombre == av_ref:
                print("No puedes tener dos aviones con el mismo call-sign en una misma operación!\n")
                return None
            else:
                pass
        aux_obj = avion(aux_nombre, 5, 5, "NATO")
        print(f"{aux_nombre} está esperando en la catapulta para ser lanzado")
        del aux_obj
                
    else:
        pass

    if CommandLine[0:10] == "/modificar":
        segundo_argumento = CommandLine[11:]
        aux_avion_select = ""
        if segundo_argumento == "":
            return None
        if segundo_argumento in DictAmigable:
            aux_avion_select = segundo_argumento
        else:
            print(f"El avión {segundo_argumento} no pertenece a la operación, quizas te has equivocado de nombre capitan...")
            CommandLine = ""
            return None
        CommandLine = input("Que deseas mejorar, el FUSELAJE o el ARMAMENTO?...escribelo literalmente: ")
        if CommandLine == "FUSELAJE" or CommandLine == "fuselaje":
            aux_fuselaje = DictAmigable[aux_avion_select].av_vida
            MissionClearing(ActualMission)
            print(f"\nActualmente tu {aux_avion_select} tiene los siguientes puntos de fuselaje: {aux_fuselaje}\nCada pto de fuselaje adicional cuesta 10M de dolares")
            try:
                CommandLine = int(input("cuantos puntos de fuselaje desea añadir?: "))
                DictAmigable[aux_avion_select].av_vida = (CommandLine, False)
            except:
                print("El fuselaje añadido adicional debe ser un numero!")
        elif CommandLine == "ARMAMENTO" or CommandLine == "armamento":
            aux_armamento = DictAmigable[aux_avion_select].av_ataque
            MissionClearing(ActualMission)
            print(f"\nActualmente tu {aux_avion_select} tiene los siguientes puntos de armamento: {aux_armamento}\nCada pto de armamento adicional cuesta 10M de dolares")
            try:
                CommandLine = int(input("cuantos puntos de armamento desea añadir?: "))
                DictAmigable[aux_avion_select].av_ataque = CommandLine
            except:
                print("El armamento añadido adicional debe ser un numero!")
        else:
            print(f"{CommandLine} no es un parametro que pueda ser modificado!")
        CommandLine = "" # añadimos esto por que los siguientes bloques requieren slicing de strings, pero en este if hemos usado commandline para los inputs que vuelven a
        #la variable una int, y el slicing no se puede hacer en ints asi que crasheara, la solución más rápida es simplemente asegurarnos de que CommandLine esta vacia al terminar.
    else:
        pass

    if CommandLine[0:11] == "/decomision":
        segundo_argumento_2 = CommandLine[12:]
        aux_avion_select = ""
        if segundo_argumento_2 in DictAmigable:
            aux_avion_select = segundo_argumento_2
        else:
            print(f"El avión {segundo_argumento_2} no pertenece a la operación, quizas te has equivocado de nombre capitan...")
            CommandLine = ""
            return None
        del DictAmigable[segundo_argumento_2]
        MissionClearing(ActualMission)
        print(f"El avión {segundo_argumento_2} ha sido eliminado de la operación y se ha reembolsado su coste en el presupuesto")
        Dinero += 20
        CommandLine = ""
    else:
        pass

    # OPERACIÓN

    if CommandLine == "/catapultar":
        aux_del_list_ally = []
        aux_del_list_enemy = []
        total_list_derribados = []
        total_list_derribos_aliados = []
        ScreenClearing()
        time.sleep(1)
        print("Comenzando la Operación....")
        for aviones in DictAmigable:
            time.sleep(1)
            print(f"{aviones}.............HA DESPEGADO")
        print("\nEstado de la Operación: En Curso...")
        time.sleep(15)
        contador_daño_aliado = 0
        contador_daño_enemigo = 0
        for av_aliado in DictAmigable:
            contador_daño_aliado += DictAmigable[av_aliado].av_ataque
        for av_enemigo in DictEnemigos:
            contador_daño_enemigo += DictEnemigos[av_enemigo].av_ataque
            
        while DictAmigable != {} and DictEnemigos != {}:
            for eachavion in DictAmigable:
                DictAmigable[eachavion].av_vida = (contador_daño_enemigo, True)
                if DictAmigable[eachavion].av_vida <= 0:
                    aux_del_list_ally.append(eachavion)
                    total_list_derribos_aliados.append(eachavion)
                    
            for eachavion in DictEnemigos:
                DictEnemigos[eachavion].av_vida = (contador_daño_aliado, True)
                if DictEnemigos[eachavion].av_vida <= 0:
                    aux_del_list_enemy.append(eachavion)
                    total_list_derribados.append(eachavion)
                    
            for eachavion in aux_del_list_ally:
                del DictAmigable[eachavion]
            for eachavion in aux_del_list_enemy:
                del DictEnemigos[eachavion]
            aux_del_list_ally = []
            aux_del_list_enemy = []      
        ScreenClearing()
        if DictAmigable != {}:
            if mision != 10:
                print(" /$$    /$$ /$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$  /$$     /$$\n| $$   | $$|_  $$_/ /$$__  $$|__  $$__//$$__  $$| $$__  $$|  $$   /$$/\n| $$   | $$  | $$  | $$  \\__/   | $$  | $$  \\ $$| $$  \\ $$ \\  $$ /$$/ \n|  $$ / $$/  | $$  | $$         | $$  | $$  | $$| $$$$$$$/  \\  $$$$/  \n \\  $$ $$/   | $$  | $$         | $$  | $$  | $$| $$__  $$   \\  $$/   \n  \\  $$$/    | $$  | $$    $$   | $$  | $$  | $$| $$  \\ $$    | $$    \n   \\  $/    /$$$$$$|  $$$$$$/   | $$  |  $$$$$$/| $$  | $$    | $$    \n    \\_/    |______/ \\______/    |__/   \\______/ |__/  |__/    |__/    \n")
                for eachavion in total_list_derribados:
                    print(f"{eachavion}................DERRIBADO - ENEMIGO")
                for eachavion in total_list_derribos_aliados:
                    print(f"{eachavion}................DERRIBADO - ALIADO")
                print(f"\n\nBien hecho cápitan, nuestra victoria nos ha dado {Bounty}M de dolares en presupuesto, estemos alerta, el golfo persico es peligroso...")
                input("\nPulse cualquier tecla para continuar...")
                Dinero += Bounty
                mision += 1
                mission_guider()
            else:
                print(" /$$    /$$ /$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$  /$$     /$$\n| $$   | $$|_  $$_/ /$$__  $$|__  $$__//$$__  $$| $$__  $$|  $$   /$$/\n| $$   | $$  | $$  | $$  \\__/   | $$  | $$  \\ $$| $$  \\ $$ \\  $$ /$$/ \n|  $$ / $$/  | $$  | $$         | $$  | $$  | $$| $$$$$$$/  \\  $$$$/  \n \\  $$ $$/   | $$  | $$         | $$  | $$  | $$| $$__  $$   \\  $$/   \n  \\  $$$/    | $$  | $$    $$   | $$  | $$  | $$| $$  \\ $$    | $$    \n   \\  $/    /$$$$$$|  $$$$$$/   | $$  |  $$$$$$/| $$  | $$    | $$    \n    \\_/    |______/ \\______/    |__/   \\______/ |__/  |__/    |__/    \n")
                for eachavion in total_list_derribados:
                    print(f"{eachavion}................DERRIBADO - ENEMIGO")
                for eachavion in total_list_derribos_aliados:
                    print(f"{eachavion}................DERRIBADO - ALIADO")
                input("\nPulse cualquier tecla para continuar...")
                Dinero += Bounty
                ending()
                
        else:
            print("       /$$             /$$$$$$                      /$$          \n      | $$            /$$__  $$                    | $$          \n  /$$$$$$$  /$$$$$$ | $$  \\__//$$$$$$   /$$$$$$  /$$$$$$         \n /$$__  $$ /$$__  $$| $$$$   /$$__  $$ |____  $$|_  $$_/         \n| $$  | $$| $$$$$$$$| $$_/  | $$$$$$$$  /$$$$$$$  | $$           \n| $$  | $$| $$_____/| $$    | $$_____/ /$$__  $$  | $$ /$$       \n|  $$$$$$$|  $$$$$$$| $$    |  $$$$$$$|  $$$$$$$  |  $$$$/       \n \\_______/ \\_______/|__/     \\_______/ \\_______/   \\___/         \n")
            for eachavion in total_list_derribados:
                print(f"{eachavion}................DERRIBADO - ENEMIGO")
            for eachavion in total_list_derribos_aliados:
                print(f"{eachavion}................DERRIBADO - ALIADO")
            print(f"\nMala suerte cápitan... Hemos perdido la batalla, todavía podemos detenerlos, nos han reestablecido el presupuesto, vamos a intentarlo de nuevo...")
            input("\nPulse cualquier tecla para continuar...")
            reset_the_scene()
        total_list_derribados = []
        total_list_derribos_aliados = []
            
            
        

    

    return None

# This starts the program.

history()

while True:
    NewCommand()
    
    
        
        
