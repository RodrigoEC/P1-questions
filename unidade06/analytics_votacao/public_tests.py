#!/usr/bin/env python
# coding: utf-8
import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
conta_votos = getattr(undertest, 'conta_votos', None)

class PublicTests(unittest.TestCase):

    def test_simples(self):
        votacao = []
        votacao.append('uma,543,joao,PPPP,sim')
        assert conta_votos(votacao, 543) == [1,0]

    def test_exemplo(self):
        votacao = []
        votacao.append('uma,543,joao,PPPP,sim')
        votacao.append('uma,543,marina,PPPP,nao')
        votacao.append('uma,5,joao,PPPP,sim')
        votacao.append('uma,543,julio,P,nao')
        votacao.append('uma,543,carlos,PBBBB,sim')
        votacao.append('uma,543,juliana,PP,sim')
        votacao.append('uma,99,joao,PPPP,sim')

        assert conta_votos(votacao, 543) == [3,2]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
