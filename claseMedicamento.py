class Medicamento:
    __idCama = None
    __idMedicamento = None
    __nombreComercial = None
    __monodroga = None
    __presentacion = None
    __cantidadAplicada = None
    __precioTotal = None

    def __init__(self, idcama = None, idmedicamento = None, nombreComercial = None, monodroga = None, presentacion = None, cantidad = None, precio = None):
        if idmedicamento >= 1 and idmedicamento <= 100:
            self.__idCama = idcama
            self.__idMedicamento = idmedicamento
            self.__nombreComercial = nombreComercial
            self.__monodroga = monodroga
            self.__presentacion = presentacion
            self.__cantidadAplicada = cantidad
            self.__precioTotal = precio
        else:
            print('ERROR: No puede crearse esa instancia!')

    def __str__(self):
        return 'Cama: {}, medicamento id: {}, nombre comercial: {}, monodroga: {}, presentacion: {}, cantidad aplicada: {}, precio total: {}'. format(self.__idCama, self.__idMedicamento, self.__nombreComercial, self.__monodroga, self.__presentacion, self.__cantidadAplicada, self.__precioTotal)
                
    def getIDCama(self):
        return self.__idCama

    def getNombreComercial(self):
        return self.__nombreComercial

    def getMonodroga(self):
        return self.__monodroga

    def getPresentacion(self):
        return self.__presentacion

    def getCantidadAplicada(self):
        return self.__cantidadAplicada

    def getPrecio(self):
        return self.__precioTotal