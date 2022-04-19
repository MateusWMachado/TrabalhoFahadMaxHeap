from maxHeap import *
import os
from time import sleep

clear = lambda: os.system('cls')

class Pessoa:
    def __init__(self, nome_completo, tipo_sanguineo, data_nascimento):
        self.nome_completo = nome_completo
        self.tipo_sanguineo = tipo_sanguineo
        self.data_nascimento = data_nascimento

if __name__ == "__main__":
    h = MaxHeap()
    aux = []
    contador = 999
    while True:
        print("1 - Novo Paciente")
        print("2 - Chamar novo paciente")
        print("3 - Ver o proximo paciente a ser chamado")
        print("4 - Listar os ultimos 5 pacientes chamados")
        print("5 - Sair")                                
        menu = int(input())
        if menu == 1:
            clear()            
            nomeCompleto = str(input("Qual o nome do paciente? "))
            tipoSanguineo = str(input("Tipo sanguineo? "))
            dataNascimento = str(input("Data de nascimento? "))
            prioridade = int(input("Qual a ordem de prioridade do paciente? (1 a 10) "))

            newPerson = Pessoa(nomeCompleto, tipoSanguineo, dataNascimento)
            newPacient = (prioridade, contador, (newPerson.nome_completo, newPerson.tipo_sanguineo, newPerson.data_nascimento))

            h.put(newPacient)
            contador -= 1
            clear()
        if menu == 2:
            clear()  
            aux.append(h.peek())
            print(h.get())
            sleep(3)
            clear()
        if menu == 3:
            clear()
            print(h.peek())
            sleep(3)
            clear()
        if menu == 4:
            clear() 
            while len(aux) > 5:
                aux.pop(0)
            for i in range(len(aux)):
                print(aux[i])
            sleep(3)
            clear()
        if menu == 5:
            break

            
                
                
