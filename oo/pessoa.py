class Pessoa:
    def __init__(self, nome=None, idade=18):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    p = Pessoa('Cadu')
    print(p.cumprimentar())
