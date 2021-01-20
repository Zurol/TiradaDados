import tkinter as tk
import random
from tkinter import messagebox
import tkinter.font as font
from tkinter import simpledialog

cuadricula = []

def activar(indice):
    print(indice)
    #print(jugador.getName())
    if Juego.jugadores[indice].getStatus() :
        Juego.jugadores[indice].setStatus(False)
    else :
        Juego.jugadores[indice].setStatus(True)
    #jugador.status = True
    actualizarTablero()
    #pintarJugadores(50, 200)

def actualizarTablero():
    #for x in range(len(cuadricula)):
    #   print(cuadricula[x])

    pintarJugadores(50, 200)


def pintarJugadores(posX, posY):

    y=0

    #posX = (width - (70 * len(Juego.getPlayers())))/2

    for x in range(len(Juego.getPlayers())):
        colorStatus = '#FFF'
        if Juego.jugadores[x].status :
            colorStatus = '#DF0'

        if Juego.jugadores[x] == Juego.lastWinner:
            colorLabel = '#0F0'
        elif Juego.jugadores[x].status:
            colorLabel = '#ccc'
        else :
            colorLabel = '#fff'


        if x==0:
            cuadricula.append(tk.Button(root, command=lambda: activar(0), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + x*70), y=(posY + y*70)))
        elif x==1:
            cuadricula.append(tk.Button(root, command=lambda: activar(1), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + x*70), y=(posY + y*70)))
        elif x==2:
            cuadricula.append(tk.Button(root, command=lambda: activar(2), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + x*70), y=(posY + y*70)))
        elif x==3:
            cuadricula.append(tk.Button(root, command=lambda: activar(3), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + x*70), y=(posY + y*70)))
        elif x==4:
            cuadricula.append(tk.Button(root, command=lambda: activar(4), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + x*70), y=(posY + y*70)))
        elif x==5:
            cuadricula.append(tk.Button(root, command=lambda: activar(5), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + x*70), y=(posY + y*70)))
        elif x==6:
            cuadricula.append(tk.Button(root, command=lambda: activar(6), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + x*70), y=(posY + y*70)))
        elif x==7:
            cuadricula.append(tk.Button(root, command=lambda: activar(7), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + x*70), y=(posY + y*70)))
        elif x==8:
            cuadricula.append(tk.Button(root, command=lambda: activar(8), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + (x%7)*70), y=(posY + y*70)))
        elif x==9:
            cuadricula.append(tk.Button(root, command=lambda: activar(9), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + (x%7)*70), y=(posY + (y+1)*70)))
        elif x==10:
            cuadricula.append(tk.Button(root, command=lambda: activar(10), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + (x%7)*70), y=(posY + (y+1)*70)))
        elif x==11:
            cuadricula.append(tk.Button(root, command=lambda: activar(11), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + (x%7)*70), y=(posY + (y+1)*70)))
        elif x==12:
            cuadricula.append(tk.Button(root, command=lambda: activar(12), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + (x%7)*70), y=(posY + (y+1)*70)))
        else:
            cuadricula.append(tk.Button(root, command=lambda: activar(("{0}".format(x))), text=("{0}".format(Juego.jugadores[x].getName())), width=8, heigh=4, bg=colorStatus).place(x=(posX + (x%7)*70), y=(posY + (y+1)*70)))

        tk.Label(root, text=("P({0})\n W[{1}] L[{2}]".format(x, Juego.jugadores[x].getWins(), Juego.jugadores[x].getLoses())), width=8, heigh=2, bg=colorLabel).place(x=(posX + 2 + (x%8)*70), y=(posY + 5 + (y+1)*70))

        numeroDado = ""

        if Juego.jugadores[x].status:
            numeroDado = Juego.jugadores[x].getDice().getValue()


        tk.Label(root, text=("{0}".format(numeroDado)), width=8, heigh=4, bg=colorLabel).place(x=(posX + 2 + (x%8)*70), y=(posY + 120 + (y)*70))




# Función reiniciar los valores a por defecto y los elementos visuales
# al estado inicial.
#
def startGame():
    print("Iniciando el juego")
    startButton.configure(state='disabled', bg='#424251', fg='#FFF')
    entry.configure(state='disabled', bg='#424251', fg='#FFF')
    moveButton.configure(state='normal', bg='#FFF', fg='#000')
    Jugador = Player(entry.get())
    JugadorIA1 = Player("A1")
    JugadorIA2 = Player("A2")
    JugadorIA3 = Player("A3")

    Juego.addPlayer(Jugador)
    Juego.addPlayer(JugadorIA1)
    Juego.addPlayer(JugadorIA2)
    Juego.addPlayer(JugadorIA3)

    pintarJugadores(50, 200)

def addPlayer():
    nombreJugador = simpledialog.askstring("Input", "¿Cuál es el nombre del nuevo jugador?",
                                    parent=root)

    nuevoJugador = Player(nombreJugador)
    Juego.addPlayer(nuevoJugador)
    actualizarTablero()

def movementGame():
    print("[MOVIMIENTO]")
    Juego.groupMovement()



def getWinner(players):
    ganador = None
    valorMaximo = 0
    empate = False
    jugadoresEmpatados = []


    for y in range(len(players)):
        players[y].getDice().rollDice()
        #print(players[y].getName())
        print("{0} tiró un {1}".format(players[y].getName(), players[y].getDice().getValue()))
        players[y].updateValues()

        if players[y].getDice().getValue() > valorMaximo:
            valorMaximo = players[y].getDice().getValue()
            ganador = players[y].getName()
            indiceGanador = y
            jugadoresEmpatados = []
            empate = False
            jugadoresEmpatados.append(players[y])

        elif players[y].getDice().getValue() == valorMaximo:
            print("Hubo un empate entre {0} y {1}.".format(ganador, players[y].getName()))
            empate = True
            jugadoresEmpatados.append(players[y])

    if empate:
        print("Desempate!")
        print("Número de jugadores empatados: {0}".format(len(jugadoresEmpatados)))
        ganador = getWinner(jugadoresEmpatados)

    else:
        print("El ganador es: {0}\n".format(ganador))
        players[indiceGanador].addWin()
        Juego.setLastWiner(players[indiceGanador])
        actualizarTablero()

class game():
    jugadores = []
    lastWinner = None

    def addPlayer(self, player):
        self.jugadores.append(player);

    def getPlayers(self):
        '''
        for y in range(len(self.jugadores)):
            print(self.jugadores[y])
            print(self.jugadores[y].getName())
        '''
        return self.jugadores

    def groupMovement(self):
        ganador = None
        #valorMaximo = 0
        #empate = False
        #jugadoresEmpatados = []

        print("[MOVIMIENTO GRUPAL]")

        jugadoresActivos = []

        print(len(self.getPlayers()))

        for indiceJugador in range(len(self.getPlayers())):
            print("IndiceJugador {0}".format(indiceJugador))
            #print("Objeto",self.jugadores[indiceJugador])
            #print(".Status",self.jugadores[indiceJugador].status)
            #print("getStatus()",self.jugadores[indiceJugador].getStatus())
            if self.jugadores[indiceJugador].getStatus():
                jugadoresActivos.append(self.jugadores[indiceJugador])

        ganador = getWinner(jugadoresActivos)

    def setLastWiner(self, player):
        self.lastWinner = player


#
# Class Dice
# @rollDice
class Dice():
    value = None
    faces = 0

    def __init__(self, faces=6):
        self.faces = faces

    def rollDice(self):
        #print("Tirando Dado")
        self.value = random.randrange(1, self.faces)

    def getValue(self):
        return self.value

#
# Class Player
# @setName
# @getName
# @
class Player():
    name = ""
    wins = 0
    loses = 0
    minValue = 6
    maxVaule = 0
    status = False
    dice = None

    def __init__(self, name=""):
        self.name = name
        self.dice = Dice()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getWins(self):
        return self.wins

    def addWin(self):
        self.wins += 1
        print("Las victorias aumentan a {0}".format(self.wins))

    def getLoses(self):
        return self.loses

    def addLose(self):
        self.loses += 1

    def getDice(self):
        return self.dice

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status
        print(self)

    def updateValues(self):
        if self.minValue > self.getDice().getValue() :
            self.minValue = self.getDice().getValue()
            print("Nuevo mínimo actualizado para {0} a {1}.".format(self.getName(), self.getDice().getValue()))

        if self.maxVaule < self.getDice().getValue() :
            self.maxVaule = self.getDice().getValue()
            print("Nuevo máximo actualizado para {0} a {1}.".format(self.getName(), self.getDice().getValue()))


Juego = game()


#print(Juego)
#Juego.getPlayers()
'''
print("\nTirada #1")
Juego.groupMovement()
print("\nTirada #2")
Juego.groupMovement()
print("\nTirada #3")
Juego.groupMovement()
print("\nTirada #4")
Juego.groupMovement()
'''



heigh = 500
width = 700
widthInput = 16

root = tk.Tk()
root.config(width=width, height=heigh, bg='white')

startTitle = tk.Label(root, text="JUEGO DE DADOS", width=widthInput)
startTitle.config(font=("Courier", 44), bg='white')
startTitle.place(x=75, y=40)

playerLabel = tk.Label(root, text="Nombre del jugador:", width=widthInput)
playerLabel.config(font=(12))
playerLabel.place(x=100, y=140)

entry = tk.Entry(root, justify = tk.CENTER, width=widthInput)
entry.config(font=(12))
entry.place(x=300, y=140)


startButton = tk.Button(root, text="Iniciar el juego",
    command=lambda: startGame())
#startButton.config(font=(1))
startButton.place(x=500, y=140)

addButton = tk.Button(root, text="+",
    command=lambda: addPlayer())
#addButton.config(font=(1))
addButton.place(x=600, y=140)

moveButton = tk.Button(root, text="Tirada",
    command=lambda: movementGame())
moveButton.config(font=(6))
moveButton.configure(state='disabled')
moveButton.place(x=(width/2-50), y=400)



root.mainloop()