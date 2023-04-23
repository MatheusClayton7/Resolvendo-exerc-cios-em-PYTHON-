#Classes e metodos 
# Sintaxe

#Marca, Memoria Ram, Placa de vídeo

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    pass

    def Ligar(self):
        print('Estou Ligando')

    def Desligar(self):
        print('Estou desligando')

    def ExibirInformaçõesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)        

computador1 = Computador('Lenovo','8GB','Intel Graphics')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformaçõesDesteComputador()