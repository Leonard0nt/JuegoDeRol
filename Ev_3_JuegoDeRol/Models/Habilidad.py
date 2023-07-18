class Habilidad:
    def __init__(self):
        self._nombreHabilidad = ""
        self._descripcionHabilidad = ""
    
    """
    Metodos get
    """
    def getNombreHabilidad(self):
        return self._nombreHabilidad
    
    def getDescripcionHabilidad(self):
        return self._descripcionHabilidad
    
    """
    Metodos set
    """
    def setNombreHabilidad(self,nvoNombre):
        self._nombreHabilidad = nvoNombre
    
    def setDescripcionHabilidad(self,nvaDescripcion):
        self._descripcionHabilidad = nvaDescripcion
    
    def toString(self):
        return f"""Nombre: {self._nombreHabilidad}//Descripcion: {self._descripcionHabilidad}
        -----------------------------
        """