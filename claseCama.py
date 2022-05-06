class Cama:
    __idCama = None
    __habitacion = None
    __estado = None
    __nombreApellido = None
    __diagnostico = None
    __fecha_internacion = None
    __fecha_alta = None

    def __init__(self, idcama = None, habitacion = None, estado = False, nombre = None ,diagnostico = None, fechaInt = None, fecha_Alta = None):
        if idcama >= 1 and idcama <= 30:
            if not estado:#desocupada
                self.__idCama = idcama
                self.__habitacion = habitacion
                self.__estado = estado
                self.__nombreApellido = None
                self.__fecha_internacion = fechaInt
                self.__fecha_alta = fecha_Alta
            else:
                self.__idCama = idcama
                self.__habitacion = habitacion
                self.__estado = estado
                self.__nombreApellido = nombre
                self.__diagnostico = diagnostico
                self.__fecha_internacion = fechaInt
                self.__fecha_alta = fecha_Alta
        else:
            print('ERROR: No puede crearse esa instancia!')

    def __str__(self):       
        return 'Cama: {} Habitacion: {} Nombre del paciente: {} fecha de internacion: {}' .format(self.__idCama,self.__habitacion,self.__nombreApellido,self.__fecha_internacion)

    def getNombrePaciente(self):
        return self.__nombreApellido

    def getIDCama(self):
        return self.__idCama

    def getHabitacion(self):
        return self.__habitacion

    def getDiagnostico(self):
        return self.__diagnostico

    def getFechaInternacion(self):
        return self.__fecha_internacion

    def setFechaAlta(self, unaFecha):
        self.__fecha_alta = unaFecha

    def getFechaAlta(self):
        return self.__fecha_alta
    
    def DesocuparCama(self):
        self.__estado = False
        self.__nombreApellido = None
        
        

            










