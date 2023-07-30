# Autor: giovanels
# TODO: mudar de snake_case para PascalCase

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
    def get_modelo(self):
        return self._modelo

    def get_marca(self):
        return self._marca

    def get_ano(self):
        return self._ano

    def get_cor(self):
        return self._cor

    def get_preco(self):
        return self._preco

    def get_placa(self):
        return self._placa

    def get_km_rodado(self):
        return self._km_rodado

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_marca(self, marca):
        self._marca = marca

    def set_ano(self, ano):
        self._ano = ano

    def set_cor(self, cor):
        self._cor = cor

    def set_preco(self, preco):
        self._preco = preco

    def set_placa(self, placa):
        self._placa = placa

    def set_km_rodado(self, km_rodado):
        self._km_rodado = km_rodado
