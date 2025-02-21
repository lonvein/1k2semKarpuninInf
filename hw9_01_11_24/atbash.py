class Atbash:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self):
        lowercase_code = {x: y for x, y in zip(self.alphabet, self.alphabet[::-1])}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, self.alphabet[::-1])}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])


cipher = Atbash()
line = "Жцко Иъчяоа — вмр эцы жцкоя прынмясрэфц, э фрмрорт фяшыдх нцтэру э рмфодмрт мъфнмъ чятъсаъмна нцтэрурт, сяйрыаёцтна ся съфрмрорт прнмрассрт зцнуъ прчцицх уъэъъ цуц пояэъъ съьр э яукяэцмъ. Сяпоцтъо, э жцкоъ нр ныэцьрт эпояэр ся 3, Я юдуя юд чятъсъся ся Ь, Ю нмясъм Ы, ц мяф ыяуъъ. Жцко сячэяс э зънмг оцтнфрьр цтпъоямроя Ьяа Буца Иъчяоа, цнпругчрэяэжъьр ъьр ыуа нъфоъмсрх пъоъпцнфц нр нэрцтц ьъсъояуятц. Нуъылбёяа зянмг ояюрмд чяжцкорэяся жцкорт Иъчяоа. Ырпцжцмъ тъмры decode ц оянжцколхмъ нуъылбёцх оячыъу уяюроямросрх ояюрмд. Прылтяхмъ, прзътл эят съ нррюёцуц фубз жцкорэясца ц змр эят н вмцт ыъуямг"
while line != '.':
    print(cipher.encode(line))
    line = input()