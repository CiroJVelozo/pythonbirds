class Pessoa:
    def __init__(self, nome = None,idade = None):
        self.nome = nome
        self.idade = idade

    def comprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
     p = Pessoa('Ciro',25)

     print(Pessoa.comprimentar(p))
     print(id(p))
     print(p.comprimentar())
     print(p.nome)
     print(p.idade)
