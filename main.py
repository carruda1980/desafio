# Em Python não existe atributos privados propriamente ditos, o que existe é uma convenção
# Tambem não se utiliza metodos getter e setters
# Em Python existe um metodo que se nao me engano é o construct, porem é mais comum utilizar o __init__ para inicializar
# valores da classe


class Jogo:
    def __init__(self, quantidade_dezenas, total_jogos):
        self.__quantidade_dezenas = quantidade_dezenas
        self.__resultado = 0
        self.__total_jogos = total_jogos
        self.__jogos = 0

    def get__resultado(self):
        return self.__resultado

    def set__resultado(self, resultado):
        self.__resultado = resultado

    def get__total_jogos(self):
        return self.__total_jogos

    def set__total_jogos(self, total_jogos):
        self.__total_jogos = total_jogos

