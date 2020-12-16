# Em Python não existe atributos privados propriamente ditos, o que existe é uma convenção
# Tambem não se utiliza metodos getter e setters
class Jogo:
    __quantidade_dezenas = [6,7,8,9]
    __resultado = 0
    __total_jogos = 0
    __jogos = 0

    def get__resultado(self):
        return self.__resultado

    def set__resultado(self, resultado):
        self.__resultado = resultado

    def get__total_jogos(self):
        return self.__total_jogos

    def set__total_jogos(self, total_jogos):
        self.__total_jogos = total_jogos

