class Pessoa:

    olhos = 2

    def __init__(self,*filho, nome = None,idade = None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filho)

    def comprimentar(self):
        return f'Ola {id(self)}'
    @staticmethod
    def metodo_estatico():
        return 42
    #é usado classmethod quando se quer usar os conteudos da classe
    @classmethod
    def nome_e_atributos_da_classe(cls):
        return f'{cls}, olhos={cls.olhos}'

class  Homem(Pessoa):
    pass

if __name__ == '__main__':

     jose = Pessoa( nome='José',idade=25)

     ciro = Homem(jose,nome='Ciro',idade=25)
     #inserindo atributo dinamico no objeto ciro
     ciro.sobrenome = 'josé velozo'

     print(Pessoa.comprimentar(ciro))
     #print(id(ciro))
     #print(ciro.comprimentar())
     #print(ciro.nome)
     #print(ciro.idade)
     print(ciro.filhos)
     print(ciro.sobrenome)

     print(ciro.__dict__)
     print()
     print(jose.__dict__)
     #deletando dinamicamente um atributo de um objeto , pode deletar qualquer atributo
     del ciro.sobrenome

     print(ciro.olhos)
     print(jose.olhos)


