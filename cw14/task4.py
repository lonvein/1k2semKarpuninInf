import unittest


class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            decoded = self.alphabet[(i - key) % len(self.alphabet)]
            self._decode[letter] = decoded
            self._decode[letter.upper()] = decoded.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._decode.get(char, char) for char in line])
        
class TestText(unittest.TestCase):
    def test_cesar(self):
        key = 412
        cipher = Caesar(key)
        self.assertEqual(cipher.decode("проверка"), "яаюсфаъп", f"cipher.decode('проверка') = {cipher.decode(" проверка")} should be 'яаюсфаъп'")
class TestPaarsaf(unittest.TestCase):
    def test_cesar(self):
        key = 666
        cipher = Caesar(key)
        self.assertEqual(cipher.decode("Эбэмэ проверрррка фв121 2 оатфдтыадлтфдауьлтцшанфгниофрииоб тфф"), "Гжгтг хцфзкццццрё ъз121 2 фёшъйшбёйсшъйёщвсшьюёуъиуофъцоофж шъъ", f"cipher.decode('Эбэмэ проверрррка фв121 2 оатфдтыадлтфдауьлтцшанфгниофрииоб тфф') = {cipher.decode("Эбэмэ проверрррка фв121 2 оатфдтыадлтфдауьлтцшанфгниофрииоб тфф")} should be 'Гжгтг хцфзкццццрё ъз121 2 фёшъйшбёйсшъйёщвсшьюёуъиуофъцоофж шъъ'")

key = int(input('Введите ключ:'))
cipher = Caesar(key)
line = input()
print(cipher.decode(line))


if __name__ == '__main__':
    unittest.main()
    

