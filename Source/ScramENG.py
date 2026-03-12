# --------------------------------------------------------------------
# SCRAM SBU PROJECT, BY SIXTINA STUDIO 2026, DEVELOPED BY MARCOKISTAN
# --------------------------------------------------------------------

"""This project was created for the purpose of learning Object-Oriented Programming.
It has served me personally, and in the process, I managed to create a fairly
interesting video game, even though its interface is based on SHELL BASED UI.

SCRAM SBU uses part of the Benux 2.0 code to control the command system.
It works with a while loop that constantly waits for a new command in each iteration.

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
            print("\nWe have run out of budget!")
        else:
            Dinero = Dinero - dinero_a_gastar
            self._ataque = self._ataque + ataque
            print(f"\n{self._nombre} now has {self._ataque} Weaponry Pts!")
            
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
                print("\nWe have run out of budget!")
            else:
                Dinero = Dinero - dinero_a_gastar
                self._vida += vida
                print(f"{self._nombre} now has {self._vida} Hull Pts!")
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
            CommandLine = input(f"Budget -> {Dinero}M >: ")
        Executer()
    except:
        NewCommand()

def history():
    ScreenClearing()
    print("  ______    ______   _______    ______   __       __         ______   _______   __    __ \n /      \\  /      \\ /       \\  /      \\ /  \\     /  |       /      \\ /       \\ /  |  /  |\n/$$$$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$  |$$  \\   /$$ |      /$$$$$$  |$$$$$$$  |$$ |  $$ |\n$$ \\__$$/ $$ |  $$/ $$ |__$$ |$$ |__$$ |$$$  \\ /$$$ |      $$ \\__$$/ $$ |__$$ |$$ |  $$ |\n$$      \\ $$ |      $$    $$< $$    $$ |$$$$ /$$$$  |      $$      \\ $$    $$< $$ |  $$ |\n $$$$$$  |$$ |  __  $$$$$$$  |$$$$$$$$ |$$ $$ $$/$$ |       $$$$$$  |$$$$$$$  |$$ |  $$ |\n/  \\__$$ |$$ \\__/  |$$ |  $$ |$$ |  $$ |$$ |$$$/ $$ |      /  \\__$$ |$$ |__$$ |$$ \\__$$ |\n$$    $$/ $$    $$/ $$ |  $$ |$$ |  $$ |$$ | $/  $$ |      $$    $$/ $$    $$/ $$    $$/ \n $$$$$$/   $$$$$$/  $$/   $$/ $$/   $$/ $$/      $$/        $$$$$$/  $$$$$$$/   $$$$$$/  ")
    print(f"\n\nOn February 28, 2026, after weeks of anticipation, Israel and the USA\nbegin Operation Epic Fury.\n\nThis operation would mark the beginning of another war in the Middle East.\nThe United States has appointed you Chief of Operations on the USS Abraham Lincoln.\n\nYour job is to lead the aerial offensive.")
    input("\nPress Enter to continue...")
    ScreenClearing()
    print("A game created by:")
    print("\n   _____ _______   _______ _____  _   _          \n  / ____|_   _\\ \\ / /_   _|_   _|| \\ | |   /\\    \n | (___   | |  \\ V /  | |   | |  |  \\| |  /  \\   \n  \\___ \\  | |   > <   | |   | |  | . ` | / /\\ \\  \n  ____) |_| |_ / . \\  | |  _| |_ | |\\  |/ ____ \\ \n |_____/|_____/_/ \\_\\ |_| |_____||_| \\_/_/    \\_\\\n\n   _____ _______ _    _ _____ _____  ____  \n  / ____|__   __| |  | |  __ \\_   _|/ __ \\ \n | (___    | |  | |  | | |  | || | | |  | |\n  \\___ \\   | |  | |  | | |  | || | | |  | |\n  ____) |  | |  | |__| | |__| || |_| |__| |\n |_____/   |_|   \\____/|_____/_____|\\____/ \n")
    input("\nPress Enter to continue...")
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
    print("\n\nWonderful work Captain, you have fulfilled your duty perfectly. Glory to the United States of America!!!")
    print(f"{Dinero}M dollars obtained\n{total_aviones} planes put into SCRAM")
    input("Press any key to continue...")
    ScreenClearing()
    print("\n   _____ _______   _______ _____  _   _          \n  / ____|_   _\\ \\ / /_   _|_   _|| \\ | |   /\\    \n | (___   | |  \\ V /  | |   | |  |  \\| |  /  \\   \n  \\___ \\  | |   > <   | |   | |  | . ` | / /\\ \\  \n  ____) |_| |_ / . \\  | |  _| |_ | |\\  |/ ____ \\ \n |_____/|_____/_/ \\_\\ |_| |_____||_| \\_/_/    \\_\\\n\n   _____ _______ _    _ _____ _____  ____  \n  / ____|__   __| |  | |  __ \\_   _|/ __ \\ \n | (___    | |  | |  | | |  | || | | |  | |\n  \\___ \\   | |  | |  | | |  | || | | |  | |\n  ____) |  | |  | |__| | |__| || |_| |__| |\n |_____/   |_|   \\____/|_____/_____|\\____/ \n")
    print("\n\nA game made by Marco Rodríguez Acosta\n\nSixtina Studio 2026")
    input("Press any key to continue...")
    sys.exit()

def first_mission_tutorial():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    ScreenClearing()
    print(f"\n4 enemy planes detected in allied territory!\nQuick, we have to shoot them all down, Captain. I'll brief you quickly.\n\nThe budget provided by the State is: {Dinero}M Dollars.\nMoney is used to put planes into operation, arm them, improve their hull, etc.\nOur radar can detect the number of enemy planes, but\nit cannot tell us each one's statistics. Our sailors, however,\ncan give us information on the best plane detected by Radar using more orthodox methods...\n\nBefore launching an operation, you can always put more planes into service, remove them, or upgrade them.\n\nType /h to see the commands at any time...\n")
    input("Press Enter to continue...")
    counter = 0
    # creating the enemies
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("F-14", 25, 100, "EAST")
    aux_en2 = avion("F4", 15, 70, "EAST")
    aux_en3 = avion("F5", 15, 60, "EAST")
    aux_en4 = avion("MIG-29", 15, 40, "EAST")
    Dinero = DineroPrivado 
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 3000
    story1 = f"Planes Detected -> {counter}\n\n---------------------------- STATISTICS: PLANE WITH HIGHEST WEAPONRY PTS ----------------------------\n{bestname}.........Weaponry Pts: {beststat}.........Hull Pts: {besthealth}\nOther Planes: Unknown.....................................\n\nPrepare the operation; once it starts, you won't be able to modify the planes.\nType /h to see the commands.\n\n"
    MissionClearing(story1)

def second_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("F5", 15, 50, "EAST")
    aux_en2 = avion("MIG-29", 6, 70, "EAST")
    aux_en3 = avion("SU-24", 7, 60, "EAST")
    aux_en4 = avion("MIG-29-2", 8, 40, "EAST")
    aux_en5 = avion("MIG-29-3", 9, 40, "EAST")
    aux_en6 = avion("MIG-29-4", 12, 80, "EAST")
    Dinero = DineroPrivado 
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 4000
    story2 = f"Captain, our radar has caught the start of an enemy operation. Should we scram?\nPlanes Detected -> {counter}\n\n---------------------------- STATISTICS: PLANE WITH HIGHEST WEAPONRY PTS ----------------------------\n{bestname}.........Weaponry Pts: {beststat}.........Hull Pts: {besthealth}\nOther Planes: Unknown.....................................\n\nPrepare the operation; once it starts, you won't be able to modify the planes.\nType /h to see the commands.\n\n"
    MissionClearing(story2)

def third_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("F5", 12, 50, "EAST")
    aux_en2 = avion("MIG-29", 4, 70, "EAST")
    aux_en3 = avion("SU-24", 7, 60, "EAST")
    aux_en4 = avion("MIG-29-2", 28, 40, "EAST")
    aux_en5 = avion("MIG-29-3", 11, 40, "EAST")
    aux_en6 = avion("MIG-29-4", 12, 80, "EAST")
    aux_en7 = avion("F14", 12, 100, "EAST")
    Dinero = DineroPrivado 
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 5000
    story3 = f"The Persian Gulf gives us no rest. Iran has sent a few planes. Should we scram?\nPlanes Detected -> {counter}\n\n---------------------------- STATISTICS: PLANE WITH HIGHEST WEAPONRY PTS ----------------------------\n{bestname}.........Weaponry Pts: {beststat}.........Hull Pts: {besthealth}\nOther Planes: Unknown.....................................\n\nPrepare the operation; once it starts, you won't be able to modify the planes.\nType /h to see the commands.\n\n"
    MissionClearing(story3)

def fourth_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("HESA-KOWSAR", 50, 70, "EAST")
    aux_en2 = avion("F14", 20, 100, "EAST")
    Dinero = DineroPrivado 
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 2000
    story4 = f"Captain, we have detected two planes on our radar. We are informed they pose a real threat\ndespite being only two planes.\nPlanes Detected -> {counter}\n\n---------------------------- STATISTICS: PLANE WITH HIGHEST WEAPONRY PTS ----------------------------\n{bestname}.........Weaponry Pts: {beststat}.........Hull Pts: {besthealth}\nOther Planes: Unknown.....................................\n\nPrepare the operation; once it starts, you won't be able to modify the planes.\nType /h to see the commands.\n\n"
    MissionClearing(story4)

def fifth_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
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
    Dinero = DineroPrivado 
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 4000
    story5 = f"CAPTAIN! A large number of enemy planes has been detected in our direction. SCRAM SCRAM SCRAM\nPlanes Detected -> {counter}\n\n---------------------------- STATISTICS: PLANE WITH HIGHEST WEAPONRY PTS ----------------------------\n{bestname}.........Weaponry Pts: {beststat}.........Hull Pts: {besthealth}\nOther Planes: Unknown.....................................\n\nPrepare the operation; once it starts, you won't be able to modify the planes.\nType /h to see the commands.\n\n"
    MissionClearing(story5)

def sixth_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
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
    Dinero = DineroPrivado 
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 7000
    story6 = f"Planes are approaching our military bases. We MUST shoot them down!\nPlanes Detected -> {counter}\n\n---------------------------- STATISTICS: PLANE WITH HIGHEST WEAPONRY PTS ----------------------------\n{bestname}.........Weaponry Pts: {beststat}.........Hull Pts: {besthealth}\nOther Planes: Unknown.....................................\n\nPrepare the operation; once it starts, you won't be able to modify the planes.\nType /h to see the commands.\n\n"
    MissionClearing(story6)

def seven_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
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
    Dinero = DineroPrivado 
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 11000
    story7 = f"It seems Iran considers us a major target. No wonder, we've downed over 20 of their planes. More are coming Captain!\nPlanes Detected -> {counter}\n\n---------------------------- STATISTICS: PLANE WITH HIGHEST WEAPONRY PTS ----------------------------\n{bestname}.........Weaponry Pts: {beststat}.........Hull Pts: {besthealth}\nOther Planes: Unknown.....................................\n\nPrepare the operation; once it starts, you won't be able to modify the planes.\nType /h to see the commands.\n\n"
    MissionClearing(story7)

def eight_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("DRONE Shahed-136", 70, 1, "EAST")
    aux_en2 = avion("MIG-29", 4, 70, "EAST")
    aux_en3 = avion("SU-24", 7, 60, "EAST")
    aux_en4 = avion("MIG-29-2", 28, 40, "EAST")
    aux_en5 = avion("MIG-29-3", 11, 40, "EAST")
    aux_en6 = avion("MIG-29-4", 12, 80, "EAST")
    aux_en7 = avion("F14", 12, 100, "EAST")
    Dinero = DineroPrivado 
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 7000
    story8 = f"Captain, I have a feeling they're running out of planes; they're starting to send drones!\nDrones have high attack power, but very few hull points.\nPlanes Detected -> {counter}\n\n---------------------------- STATISTICS: PLANE WITH HIGHEST WEAPONRY PTS ----------------------------\n{bestname}.........Weaponry Pts: {beststat}.........Hull Pts: {besthealth}\nOther Planes: Unknown.....................................\n\nPrepare the operation; once it starts, you won't be able to modify the planes.\nType /h to see the commands.\n\n"
    MissionClearing(story8)

def nine_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    counter = 0
    DineroPrivado = Dinero
    Dinero = 90000
    aux_en1 = avion("DRONE Shahed-136", 70, 1, "EAST")
    aux_en2 = avion("DRONE Shahed-131", 70, 1, "EAST")
    aux_en3 = avion("DRONE Shahed-136b", 70, 1, "EAST")
    aux_en4 = avion("MIG-29-2", 28, 40, "EAST")
    aux_en5 = avion("MIG-29-3", 7, 40, "EAST")
    aux_en6 = avion("F4", 12, 80, "EAST")
    aux_en7 = avion("F14", 15, 100, "EAST")
    Dinero = DineroPrivado 
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 8000
    story9 = f"More drones are approaching, they are more SHAHEDs, scram!\nPlanes Detected -> {counter}\n\n---------------------------- STATISTICS: PLANE WITH HIGHEST WEAPONRY PTS ----------------------------\n{bestname}.........Weaponry Pts: {beststat}.........Hull Pts: {besthealth}\nOther Planes: Unknown.....................................\n\nPrepare the operation; once it starts, you won't be able to modify the planes.\nType /h to see the commands.\n\n"
    MissionClearing(story9)

def last_mision():
    global Dinero, DictAmigable, DictEnemigos, DineroPrivado, Bounty, mision
    ScreenClearing()
    time.sleep(2)
    print("Captain...\n")
    time.sleep(2)
    print("This mission is different...")
    time.sleep(2)
    print("We have to launch an attack ourselves now; we must prepare like never before.\n")
    time.sleep(5)
    counter = 0
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
    Dinero = DineroPrivado 
    for counts in DictEnemigos:
        counter += 1
    bestname, beststat, besthealth = get_best_stat()
    Bounty = 5000
    story_last = f"Captain... This mission is different...\nWe have to launch an attack ourselves now; we must prepare like never before.\n\nPlanes Detected -> {counter}\n\n---------------------------- STATISTICS: PLANE WITH HIGHEST WEAPONRY PTS ----------------------------\n{bestname}.........Weaponry Pts: {beststat}.........Hull Pts: {besthealth}\nOther Planes: Unknown.....................................\n\nPrepare the operation; once it starts, you won't be able to modify the planes.\nType /h to see the commands.\n\n"
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

    # HELP COMMANDS
    
    if CommandLine == "/h":
        MissionClearing(ActualMission)
        print("OPERATION PREPARATION:\n---------------------\n/scramjet\nYou will put a fighter jet into operation. This action costs 20M.\n\n/modify jet_name\nThe jet name follows the command. It allows modifying its HULL and ARMAMENT.\n\n/decommission jet_name\nThe jet name follows the command. It allows removing a jet from the operation.\nThe cost of putting the jet into operation is refunded.\n\nOPERATION\n---------------------\n/catapult\nLaunches the jets from the aircraft carrier and begins the operation. Type this command when you are ready.\n")
    else:
        pass

    # PRE-OPERATION

    if CommandLine == "/SCRAMJET" or CommandLine == "/scramjet":
        MissionClearing(ActualMission)
        print("Yes, my Captain!")
        aux_nombre = input("Give the plane a call-sign: ")
        for av_ref in DictAmigable:
            if aux_nombre == av_ref:
                print("You cannot have two planes with the same call-sign in the same operation!\n")
                return None
            else:
                pass
        aux_obj = avion(aux_nombre, 5, 5, "NATO")
        print(f"{aux_nombre} is waiting on the catapult to be launched.")
        del aux_obj
                
    else:
        pass

    if CommandLine[0:7] == "/modify":
        segundo_argumento = CommandLine[8:]
        aux_avion_select = ""
        if segundo_argumento == "":
            return None
        if segundo_argumento in DictAmigable:
            aux_avion_select = segundo_argumento
        else:
            print(f"The plane {segundo_argumento} does not belong to the operation. Perhaps you misspelled the name, Captain...")
            CommandLine = ""
            return None
        CommandLine = input("What do you wish to improve, the HULL or the ARMAMENT? Type it exactly: ")
        if CommandLine == "HULL" or CommandLine == "hull":
            aux_fuselaje = DictAmigable[aux_avion_select].av_vida
            MissionClearing(ActualMission)
            print(f"\nCurrently, your {aux_avion_select} has the following hull points: {aux_fuselaje}\nEach additional hull point costs 10M dollars.")
            try:
                CommandLine = int(input("How many hull points do you wish to add?: "))
                DictAmigable[aux_avion_select].av_vida = (CommandLine, False)
            except:
                print("The additional hull added must be a number!")
        elif CommandLine == "ARMAMENT" or CommandLine == "armament":
            aux_armamento = DictAmigable[aux_avion_select].av_ataque
            MissionClearing(ActualMission)
            print(f"\nCurrently, your {aux_avion_select} has the following weaponry points: {aux_armamento}\nEach additional weaponry point costs 10M dollars.")
            try:
                CommandLine = int(input("How many weaponry points do you wish to add?: "))
                DictAmigable[aux_avion_select].av_ataque = CommandLine
            except:
                print("The additional weaponry added must be a number!")
        else:
            print(f"{CommandLine} is not a parameter that can be modified!")
        CommandLine = "" 
    else:
        pass

    if CommandLine[0:13] == "/decommission":
        segundo_argumento_2 = CommandLine[14:]
        aux_avion_select = ""
        if segundo_argumento_2 in DictAmigable:
            aux_avion_select = segundo_argumento_2
        else:
            print(f"The plane {segundo_argumento_2} does not belong to the operation. Perhaps you misspelled the name, Captain...")
            CommandLine = ""
            return None
        del DictAmigable[segundo_argumento_2]
        MissionClearing(ActualMission)
        print(f"The plane {segundo_argumento_2} has been removed from the operation, and its cost has been refunded to the budget.")
        Dinero += 20
        CommandLine = ""
    else:
        pass

    # OPERATION

    if CommandLine == "/catapult":
        aux_del_list_ally = []
        aux_del_list_enemy = []
        total_list_derribados = []
        total_list_derribos_aliados = []
        ScreenClearing()
        time.sleep(1)
        print("Starting the Operation....")
        for aviones in DictAmigable:
            time.sleep(1)
            print(f"{aviones}.............HAS TAKEN OFF")
        print("\nOperation Status: In Progress...")
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
                    print(f"{eachavion}................SHOT DOWN - ENEMY")
                for eachavion in total_list_derribos_aliados:
                    print(f"{eachavion}................SHOT DOWN - ALLY")
                print(f"\n\nWell done Captain, our victory has given us {Bounty}M dollars in budget. Let's stay alert; the Persian Gulf is dangerous...")
                input("\nPress any key to continue...")
                Dinero += Bounty
                mision += 1
                mission_guider()
            else:
                print(" /$$    /$$ /$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$  /$$     /$$\n| $$   | $$|_  $$_/ /$$__  $$|__  $$__//$$__  $$| $$__  $$|  $$   /$$/\n| $$   | $$  | $$  | $$  \\__/   | $$  | $$  \\ $$| $$  \\ $$ \\  $$ /$$/ \n|  $$ / $$/  | $$  | $$         | $$  | $$  | $$| $$$$$$$/  \\  $$$$/  \n \\  $$ $$/   | $$  | $$         | $$  | $$  | $$| $$__  $$   \\  $$/   \n  \\  $$$/    | $$  | $$    $$   | $$  | $$  | $$| $$  \\ $$    | $$    \n   \\  $/    /$$$$$$|  $$$$$$/   | $$  |  $$$$$$/| $$  | $$    | $$    \n    \\_/    |______/ \\______/    |__/   \\______/ |__/  |__/    |__/    \n")
                for eachavion in total_list_derribados:
                    print(f"{eachavion}................SHOT DOWN - ENEMY")
                for eachavion in total_list_derribos_aliados:
                    print(f"{eachavion}................SHOT DOWN - ALLY")
                input("\nPress any key to continue...")
                Dinero += Bounty
                ending()
                
        else:
            print("       /$$             /$$$$$$                      /$$          \n      | $$            /$$__  $$                    | $$          \n  /$$$$$$$  /$$$$$$ | $$  \\__//$$$$$$   /$$$$$$  /$$$$$$         \n /$$__  $$ /$$__  $$| $$$$   /$$__  $$ |____  $$|_  $$_/         \n| $$  | $$| $$$$$$$$| $$_/  | $$$$$$$$  /$$$$$$$  | $$           \n| $$  | $$| $$_____/| $$    | $$_____/ /$$__  $$  | $$ /$$       \n|  $$$$$$$|  $$$$$$$| $$    |  $$$$$$$|  $$$$$$$  |  $$$$/       \n \\_______/ \\_______/|__/     \\_______/ \\_______/   \\___/         \n")
            for eachavion in total_list_derribados:
                print(f"{eachavion}................SHOT DOWN - ENEMY")
            for eachavion in total_list_derribos_aliados:
                print(f"{eachavion}................SHOT DOWN - ALLY")
            print(f"\nBad luck Captain... We have lost the battle. We can still stop them. They have restored our budget, let's try again...")
            input("\nPress any key to continue...")
            reset_the_scene()
        total_list_derribados = []
        total_list_derribos_aliados = []
        
    return None

# This starts the program.

history()

while True:
    NewCommand()
