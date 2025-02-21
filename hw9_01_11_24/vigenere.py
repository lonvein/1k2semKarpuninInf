alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    def __init__(self, keyword):
        self.alphaindex = {ch: index for index, ch in enumerate(self.alphabet)}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]

    def antic(self, letter, shift):
        if letter in self.alphaindex:  # строчная буква
            index = (self.alphaindex[letter] - shift) % len(self.alphabet)
            dletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex: # заглавная буква
            dletter = self.antic(letter.lower(), shift).upper()
        else:
            dletter = letter
        return dletter

    def decode(self, line, alphabet, k = 0):
        dtext = []
        for i, letter in enumerate(line):
            if line[i] not in alphabet:
                dtext.append(" ")
                # print(line[i], shift) - если нужно понять, как работает алгоритм
                k += 1
            else:
                shift = self.key[(i % len(self.key)) - k % len(self.key)]
                # print(line[i], shift) - аналогично
                dletter = self.antic(letter, shift)
                dtext.append(dletter)
        return ''.join(dtext)
keyword = input('keyword=')
cipher = Vigenere(keyword)
line = input()
print(cipher.decode(line, alphabet))