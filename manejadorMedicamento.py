import csv
from claseMedicamento import Medicamento
import numpy as np

class manejadorMedicamento:
    __dimension = None
    __incremento = None
    __cantidad = None
    __medicamentos = None


    def __init__(self, dimension = 10, incremento = 5):
        self.__medicamentos = np.empty(dimension,dtype = Medicamento)
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0


    def agregarMedicamento(self, unMedicamento):
        if type(unMedicamento)  == Medicamento:
            if self.__cantidad == self.__dimension:
                self.__dimension+=self.__incremento
                self.__medicamentos.resize(self.__dimension)
            self.__medicamentos[self.__cantidad] = unMedicamento
            self.__cantidad += 1

    def leerArchivo(self):
        band = False
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter = ';')

        for fila in reader:
            if not band:
                band = True
            else:
                unMedicamento = Medicamento(int(fila[0]), int(fila[1]),fila[2],fila[3],fila[4],int(fila[5]),float(fila[6]))
                self.agregarMedicamento(unMedicamento)
        archivo.close()    

    def __str__(self):
        s = ''
        for i in range(self.__cantidad):
            s+= str(self.__medicamentos[i]) + '\n'
        return s

    def mostrarDatosMedicamentos(self, idcama):
        i = 0
        total = 0
        while i < self.__cantidad:
            if self.__medicamentos[i].getIDCama() == idcama:
                if i == len(self.__medicamentos):
                    print('Medicamento/Monodroga: {}/{}\tPresentacion: {}\t\tCantidad: {}\tPrecio:{}'. format(self.__medicamentos[i].getNombreComercial(), self.__medicamentos[i].getMonodroga(),self.__medicamentos[i].getPresentacion(),self.__medicamentos[i].getCantidadAplicada(),self.__medicamentos[i].getPrecio()))
                    total += self.__medicamentos[i].getPrecio()
                else:
                    print('Medicamento/Monodroga: {}/{}\tPresentacion: {}\t\tCantidad: {}\tPrecio:{}'. format(self.__medicamentos[i].getNombreComercial(), self.__medicamentos[i].getMonodroga(),self.__medicamentos[i].getPresentacion(),self.__medicamentos[i].getCantidadAplicada(),self.__medicamentos[i].getPrecio()))
                    total += self.__medicamentos[i].getPrecio()
                    i+=1           
            else:
                i+=1

        print('Total adeudado: {}' .format(total))        