from random import sample

# Em Python não existe atributos privados propriamente ditos, o que existe é uma convenção
# Tambem não se utiliza metodos getter e setters
# Em Python existe um metodo que se nao me engano é o construct, porem é mais comum utilizar o __init__ para inicializar
# valores da classe
# Para validar as dezenas criei um metodo retornando um ValueError caso a dezena informada nao esteja na lista


class Jogo:
    def __init__(self, quantidade_dezenas, total_jogos):
        self.__quantidade_dezenas = quantidade_dezenas
        self.__resultado = 0
        self.__total_jogos = total_jogos
        self.__jogos = 3

        if not self._valida_dezenas(self.__quantidade_dezenas):
            raise ValueError("valores inválidos")

    def get__resultado(self):
        return self.__resultado

    def set__resultado(self, resultado):
        self.__resultado = resultado

    def get__total_jogos(self):
        return self.__total_jogos

    def set__total_jogos(self, total_jogos):
        self.__total_jogos = total_jogos

    def get__sorteio_sem_repeticoes(self):
        return sorted(sample(range(1, 60), self.__quantidade_dezenas))

    def set__resultado_aleatorio(self):
        self.__resultado = sorted(sample(range(1, 60), 6))

    def _valida_dezenas(self, quantidade_dezenas):
        if quantidade_dezenas not in [6,7,8,9,10]:
            return False
        else:
            return True

    def array_jogos(self):
        jogos_list = []
        for i in range(self.__total_jogos):
            novo = []
            for j in range(self.__total_jogos):
                novo.append(self.get__sorteio_sem_repeticoes())
                jogos_list.append(novo)
        return jogos_list


# Instanciando a classe passando quantidade de dezenas e total de jogos como paramentro
jogo = Jogo(6, 3)
# Sorteio sem repetições
print(jogo.get__sorteio_sem_repeticoes())
jogo.set__resultado_aleatorio()
# Resultado aleatório
print(jogo.get__resultado())
# Array de jogos
print(jogo.array_jogos())
array_jogos = jogo.array_jogos()


def html(array_jogos):
    strTable = "<html><table><tr><th>Char</th><th>ASCII</th></tr>"

    for num in array_jogos:
        strRW = "<tr><td>" + str(num) + "</td><td></tr>"
        strTable = strTable + strRW

    strTable = strTable + "</table></html>"

    hs = open("asciiCharHTMLTable.html", 'w')
    hs.write(strTable)

    return strTable


print(html(array_jogos))