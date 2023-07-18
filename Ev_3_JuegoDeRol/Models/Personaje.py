from Models.getById import *
class Personaje:
    def __init__(self):
        self._nombrePersonaje = ""
        self._habilidad = 0
        self._equipamiento = 0
        self._estado = 1
        self._raza = 0
        self._nivel = 1
    """
    Metodos get
    """
    def getNombre(self):
        return self._nombrePersonaje

    def getHabilidad(self):
        return self._habilidad

    def getEquipamiento(self):
        return self._equipamiento

    def getEstado(self):
        return self._estado

    def getRaza(self):
        return self._raza

    def getNivel(self):
        return self._nivel

    """
    Metodos set
    """
    def setNombre(self,nvoNombre):
        self._nombrePersonaje = nvoNombre

    def setHabilidad(self,nvaHabilidad):
        self._habilidad = nvaHabilidad

    def setEquipamiento(self,nvoEquipamiento):
        self._equipamiento = nvoEquipamiento

    def setEstado(self,nvoEstado):
        self._estado = nvoEstado

    def setRaza(self,nvaRaza):
        self._raza = nvaRaza

    def setNivel(self,nvoNivel):
        self._nivel = nvoNivel

    def toString(self):
        return f"""Nombre: {self._nombrePersonaje}
        Habilidad: {getNombreByIdHabilidad(self._habilidad)}
        Equipamiento: {getNombreByIdEquipamiento(self._equipamiento)}
        Estado: {getNombreByIdEstado(self._estado)}
        Raza: {getNombreByIdRaza(self._raza)}
        Nivel: {self._nivel}
        ----------------------------------------
        """
