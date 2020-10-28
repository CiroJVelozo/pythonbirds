class Pessoa:
    def __init__(self,*filho, nome = None,idade = None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filho)

    def comprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':

     jose = Pessoa()

     ciro = Pessoa(jose,nome='Ciro',idade=25)

     print(Pessoa.comprimentar(ciro))
     #print(id(ciro))
     #print(ciro.comprimentar())
     #print(ciro.nome)
     #print(ciro.idade)
     print(ciro.filhos)
