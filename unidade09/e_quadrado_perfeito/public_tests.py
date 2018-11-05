# coding: utf-8
import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
eh_quadrado_magico = getattr(undertest, 'eh_quadrado_magico', None)

class PublicTests(unittest.TestCase):
    
    def test_1(self):
        assert eh_quadrado_magico([[2,7,6],[9,5,1],[4,3,8]])

    def test_2(self):
        assert not eh_quadrado_magico([[1,2,3],[4,5,6]])

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
