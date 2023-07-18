class Raza:
    def __init__(self):
        self._nombreRaza = ""
        self._descripcionRaza = ""
    
    """
    Metodos get
    """
    def getNombreRaza(self):
        return self._nombreRaza
    
    def getDescripcionRaza(self):
        return self._descripcionRaza
    
    """
    Metodos set
    """
    def setNombreRaza(self,nvoNombre):
        self._nombreRaza = nvoNombre
    
    def setDescripcionRaza(self,nvaDescripcion):
        self._descripcionRaza = nvaDescripcion
    
    def toString(self):
        return f"""Nombre {self._nombreRaza}//Descripcion {self._descripcionRaza}
        -------------------------------
        """