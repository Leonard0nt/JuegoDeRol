class Equipamiento:
    def __init__(self):
        self._nombreEquipamiento= ""
        self._descripcionEquipamiento = ""
    
    """
    Metodos get
    """
    def getNombreEquipamiento(self):
        return self._nombreEquipamiento
    
    def getDescripcionEquipamiento(self):
        return self._descripcionEquipamiento
    
    """
    Metodos set
    """
    def setNombreEquipamiento(self,nvoNombre):
        self._nombreEquipamiento = nvoNombre
    
    def setDescripcionEquipamiento(self,nvaDescripcion):
        self._descripcionEquipamiento = nvaDescripcion
    
    def toString(self):
        return f"""Nombre: {self._nombreEquipamiento}//Descripcion: {self._descripcionEquipamiento}
        -----------------------------------------
        """
