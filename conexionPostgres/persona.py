# Clase que hará de modelo para la base de datos implemetada

class Persona(object):
  
    #Contructor
    def __init__(
        self, 
        idPersona, 
        nombre, 
        apellidoPaterno, 
        apelidoMaterno, 
        rut, 
        observacion
    ):
        self.idPersona = idPersona
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apelidoMaterno = apelidoMaterno
        self.rut = rut
        self.observacion = observacion
    
    #Metodos
    def getIdPersona(self):
        return self.idPersona
    
    def getNombre(self):
        return self.nombre

    def getApellidoPaterno(self):
        return self.apellidoPaterno

    def getApellidoMaterno(self):
        return self.apelidoMaterno

    def getRut(self):
        return self.rut

    def getObservacion(self):
        return self.observacion

    def setIdPersona(self, value):        
        self.idPersona = value

    def setNombre(self, value):        
        self.nombre = value

    def setApellidoPaterno(self, value):        
        self.apellidoPaterno = value

    def setApellidoMaterno(self, value):        
        self.apellidoMaterno = value

    def setRut(self, value):        
        self.rut = value

    def setObservacion(self, value):        
        self.observacion = value

#at = Persona(1,'as', 'as', 'as', 'as', 'as')
#print(str(at.getRut()))
#if '@' not in value:
#raise Exception("Esto no parece ser una dirección de correo")