import csv
from claseCama import Cama
from claseMedicamento import Medicamento
from manejadorMedicamento import manejadorMedicamento

class manejadorCama:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregarCama(self, unaCama):
        if type(unaCama) == Cama:
            self.__lista.append(unaCama)

    def leerArchivo(self):
        band = False
        archivo = open('camas.csv')
        reader = csv.reader(archivo, delimiter = ';')  
        for fila in reader:
            if not band:
                band = True
            else:
                nombre = fila[3]
                apellido = nombre[:nombre.find(',')]
                nombre = apellido + nombre[nombre.find(',')+1:]
                unaCama = Cama(int(fila[0]),int(fila[1]),bool(fila[2]),nombre,fila[4],fila[5],fila[6])
                self.agregarCama(unaCama)
        archivo.close()

    def __str__(self):
        s = ''
        for cama in self.__lista:
            s+= str(cama) + '\n'
        return s      

    def mostraDatosPaciente(self, nombre, manejador_medicamento):
        encontro = False
        i = 0
        while i < len(self.__lista) and not encontro:
            if self.__lista[i].getNombrePaciente().lower() == nombre.lower():
                dia = input('Ingrese el dia de alta: ')
                mes = input('Ingrese el mes de alta: ')
                anio = input('Ingrese el año de alta: ')
                fechaAlta = dia+'/'+mes+'/'+anio
                self.__lista[i].setFechaAlta(fechaAlta)
                print('== DATOS DEL PACIENTE == ')
                print('Paciente: {}\t\tCama:{}\tHabitacion: {}'. format(self.__lista[i].getNombrePaciente(), self.__lista[i].getIDCama(), self.__lista[i].getHabitacion()))
                print('Diagnostico: {}\tFecha de internacion: {}' .format(self.__lista[i].getDiagnostico(), self.__lista[i].getFechaInternacion()))
                print('Fecha de Alta: {}' .format(self.__lista[i].getFechaAlta()))
                manejador_medicamento.mostrarDatosMedicamentos(self.__lista[i].getIDCama())
                self.__lista[i].desocuparCama()
                encontro = True
            else:
                i+=1
        if i == len(self.__lista):
            print('ERROR: Paciente no encontrado!')   

    def listarporDiagnostico(self, diagnostico):
        for i in range(len(self.__lista)):
            if self.__lista[i].getDiagnostico().lower() == diagnostico.lower():
                print(self.__lista[i])




                 
