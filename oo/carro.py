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

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'

class  direcao:

    girar_a_direita_dct = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}

    girar_a_esquerda_dct = {NORTE:OESTE,OESTE:SUL,SUL:LESTE,LESTE:NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):

        self.valor = self.girar_a_direita_dct(self.valor)

        # if self.valor == NORTE:
        #     self.valor =LESTE
        # elif self.valor ==LESTE:
        #     self.valor = SUL
        # elif self.valor ==SUL:
        #     self.valor =OESTE
        # elif self.valor==OESTE:
        #     self.valor = NORTE

        return self.valor

    def girar_a_esquerda(self):

        self.valor = self.girar_a_esquerda_dct_dct(self.valor)

        # if self.valor == NORTE:
        #     self.valor =OESTE
        # elif self.valor ==OESTE:
        #     self.valor = SUL
        # elif self.valor ==SUL:
        #     self.valor =LESTE
        # elif self.valor==LESTE:
        #     self.valor = NORTE

        return self.valor

if __name__ == '__main__':
    print()