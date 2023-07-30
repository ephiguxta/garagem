# Autor: giovanels

class Veiculo:
    def __init__(self, modelo, marca, ano, cor, preco, placa, km_rodado):
        self._modelo = modelo
        self._marca = marca
        self._ano = ano
        self._cor = cor
        self._preco = preco
        self._placa = placa
        self._km_rodado = km_rodado

    #métodos setters e getters
    def getModelo(self):
        return self._modelo
    
    def setModelo(self, modelo):
        self._modelo = modelo

    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca

    def getAno(self):
       return self._ano
    
    def setAno(self, ano):
        self._ano = ano

    def getCor(self):
        return self._cor
     
    def setCor(self, cor):
        self._cor = cor

    def getPreco(self):
        return self._preco
    
    def setPreco(self, preco):
        self._preco = preco

    def getPlaca(self):
        return self._placa
    
    def setPlaca(self, placa):
        self._placa = placa

    def getKmRodado(self):
        return self._km_rodado
    
    def setKmRodado(self, km_rodado):
        self._km_rodado = km_rodado
