import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
agrupa_por_periodo = getattr(undertest, 'agrupa_por_periodo', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        turma = [
            '0511114', '0521137', '0611001',
            '0611003', '0611004', '0621006',
            '0811007', '0811009', '0811502',
            '0811604', '0811605',
        ]
        assert agrupa_por_periodo(turma) == {
            '051': 1,
            '052': 1,
            '061': 3,
            '062': 1,
            '081': 5,
        }
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
