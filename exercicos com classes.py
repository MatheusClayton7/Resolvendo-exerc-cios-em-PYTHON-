class Carro:
    def __init__(self, marca, potencia, cor):
        self.marca = marca
        self.potencia = potencia
        self.cor = cor
    pass

    def Acelerar(self):
        print('Estou acelerando')

    def Freiar(self):
        print('Estou freiando')

    def ExibirInformaçõesDesteComputador(self):
        print(self.marca, self.potencia, self.cor)        

carro1 = Carro('BMW','700CV','PRETO')
carro1.Acelerar()
carro1.Freiar()
carro1.ExibirInformaçõesDesteComputador()