from unittest import TestCase

from oo.carro import Motor

from oo.carro import Direcao

class CarroTestCase(TestCase):
    def test_velocidae_inocial(self):
        motor = Motor()
        self.assert_(0,motor.velocidade)

    def test_direcao_valor(self):
        direcao = Direcao()
        self.assert_('Norte',direcao.valor)
