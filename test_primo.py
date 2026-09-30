import unittest

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

class TestPrimo(unittest.TestCase):
    def test_numeros_primos(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertFalse(es_primo(4))

if __name__ == "__main__":
    unittest.main()
