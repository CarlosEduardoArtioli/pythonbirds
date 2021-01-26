class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=18):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    ana = Pessoa(nome='Ana')
    jose = Pessoa(nome='José')
    cadu = Mutante(ana, jose, nome='Cadu', idade=17)
    print(cadu.cumprimentar())
    for filho in cadu.filhos:
        print(filho.nome)
    cadu.sobrenome = 'Artioli'
    del cadu.filhos
    print(cadu.__dict__)
    print(jose.__dict__)
    print(Pessoa.olhos)
    print(cadu.olhos)
    print(jose.olhos)
    print(Pessoa.metodo_estatico(), cadu.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), cadu.nome_e_atributos_de_classe())
    pessoa=Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(cadu, Homem))
    print(cadu.olhos)
