from claseCama import Cama
from claseMedicamento import Medicamento
from manejadorCama import manejadorCama
from manejadorMedicamento import manejadorMedicamento

if __name__ == '__main__':
    manejador_cama = manejadorCama()
    manejador_medicamento = manejadorMedicamento()
    manejador_cama.leerArchivo()
    manejador_medicamento.leerArchivo()
    print(' == LISTA DE CAMAS == ')
    print(manejador_cama)
    print(' == LISTA DE MEDICAMENTOS==')
    print(manejador_medicamento)
    nombre_paciente = input('Ingrese el nombre de un paciente: ')
    manejador_cama.mostraDatosPaciente(nombre_paciente, manejador_medicamento)
    print('\n')
    diagnostico = input('Ingrese un diagnostico: ')
    print('== LISTA DE PACIENTES CON ESE DIAGNOSTICO ==')
    manejador_cama.listarporDiagnostico(diagnostico)

