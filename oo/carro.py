class motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade+=1

    def frear(self):

        self.velocidade -=2
        self.velocidade = max(0,self.velocidade)
        # if self.velocidade <= 1:
        #     self.velocidade = 0
        # else:
        #     self.velocidade -= 2

class  direcao:

    def __init__(self, valor = 'N'):
        self.valor = valor

    def girar_a_direita(self):

        if self.valor == 'N':
            self.valor ='L'
        elif self.valor =='L':
            self.valor = 'S'
        elif self.valor =='S':
            self.valor ='O'
        elif self.valor=='O':
            self.valor = 'N'

        return self.valor

    def girar_a_esquerda(self):

        if self.valor == 'N':
            self.valor ='O'
        elif self.valor =='O':
            self.valor = 'S'
        elif self.valor =='S':
            self.valor ='L'
        elif self.valor=='L':
            self.valor = 'N'

        return self.valor

if __name__ == '__main__':
    print()