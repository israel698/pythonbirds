class Pessoa:
    def __init__(self, *filhos, nome=None, idade= 35):
        self.nome = nome
        self.idade = idade
        self. filhos = list(filhos)

    def cumprimentar(self):
        return 'ola'

if __name__ == '__main__':
    f = Pessoa(nome='apollo')
    p = Pessoa(f, nome='israel')
    print(Pessoa.cumprimentar(p))
    print(p.nome)
    print(p.idade)
    for filho in p.filhos:
        print(filho.nome)


