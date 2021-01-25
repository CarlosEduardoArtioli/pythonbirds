class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=18):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    ana = Pessoa(nome='Ana')
    jose = Pessoa(nome='José')
    cadu = Pessoa(ana, jose, nome='Cadu', idade=17)
    print(cadu.cumprimentar())
    for filho in cadu.filhos:
        print(filho.nome)
    cadu.sobrenome = 'Artioli'
    del cadu.filhos
    jose.olhos = 1
    print(cadu.__dict__)
    print(jose.__dict__)
    print(Pessoa.olhos)
    print(cadu.olhos)
    print(jose.olhos)
