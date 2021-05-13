class Pessoa:
    dedos=20
    def __init__(self, *filhos, nome=None, idade= 23, ):
        self.nome = nome
        self.idade = idade
        self. filhos = list(filhos)

    def cumprimentar(self):
        return 'ola'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - dedos  {cls.dedos}'

if __name__ == '__main__':
    f = Pessoa(nome='apollo')
    p = Pessoa(f, nome='israel')
    print(Pessoa.cumprimentar(p))
    print(p.nome)
    print(p.idade)
    for filho in p.filhos:
        print(filho.nome)
        print(Pessoa.dedos)
        Pessoa.nariz = 1
        print(Pessoa.nariz)
        print(Pessoa.metodo_estatico(), f.metodo_estatico())
        print(Pessoa. nome_e_atributos_de_classe())