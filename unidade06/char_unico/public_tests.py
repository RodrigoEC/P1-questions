import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
char_unico = getattr(undertest, 'char_unico', None)

class PublicTests(unittest.TestCase):

   def test_basico(self):
       assert char_unico("aa***xxxzzb+++") == "b"

   def test_string_vazia(self):
       assert char_unico("kkkkrrrrgppp") == "g"

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
