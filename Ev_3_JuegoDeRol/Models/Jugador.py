class Jugador:
    def __init__(self):
        self._idJugador = 0
        self._nombreJugador = ""
        self._password = ""
        self._personaje = 0
        self._tipoJugador = ""


    """
    Metodos get
    """

    def getIdJugador(self):
        return self._idJugador

    def getNombreJugador(self):
        return self._NombreJugador

    def getPersonaje(self):
        return self._personaje

    def getTipoJugador(self):
        return self._tipoJugador

    """
    Metodos set
    """

    def setNombreJugador(self,nvoNombre):
        self._nombreJugador = nvoNombre

    def setPersonaje(self, nvoPersonaje):
        self._personaje = nvoPersonaje

    def setPassword(self, nvaContraseña):
        self._password = nvaContraseña