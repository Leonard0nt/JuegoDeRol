class Estado:
    def __init__(self):
        self._nombreEstado = ""
        self._descripcionEstado = ""
    
    """
    Metodos get
    """
    def getNombreEstado(self):
        return self._nombreEstado
    
    def getDescripcionEstado(self):
        return self._descripcionEstado
    
    """
    Metodos set
    """
    def setNombreEstado(self,nvoNombre):
        self._nombreEstado = nvoNombre
    
    def setDescripcionEstado(self,nvaDescripcion):
        self._descripcionEstado= nvaDescripcion
    
    def toString(self):
        return f"""Nombre: {self._nombreEstado}//Descripcion: {self._descripcionEstado}
        --------------------------------
        """