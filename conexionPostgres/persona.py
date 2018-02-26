# Clase que hará de modelo para la base de datos implemetada

class persona(object):

    #Atributos
    idPersona
    nombre
    apellidoPaterno
    apelidoMaterno
    rut
    observacion

    #Contructor
    def __init__(
        self, 
        idPersona,
        nombre,
        apellidoPaterno,
        apelidoMaterno,
        rut,
        observacion
    )
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