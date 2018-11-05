# coding: utf-8
import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
calcula_conta = getattr(undertest, 'calcula_conta', None)

class PublicTests(unittest.TestCase):
    
    def test_1(self):
        tabela = [["Equipamento", "Quantidade", "Tempo de Uso (horas)", "Potencia (Watts)"], ["AR-CONDICIONADO", 1, 240, 2000], ["COMPUTADOR", 2, 150, 180], ["TV", 3, 150, 110]]

        assert calcula_conta(tabela) == "R$ 163.38"

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
