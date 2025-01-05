# Moresho abeceda

alphabet = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' ',
}

# Reverse dict
alphabet_reverse = {value: key for key, value in alphabet.items()}

class Morse:
    def encode(self, text):
        """ Zakóduje text do morzeovej abecedy """
        return '  '.join(' '.join(alphabet[char] for char in word) for word in text.upper().split(' '))

    def decode(self, morse):
        """ Dekóduje morzeovú abecedu do textu """
        return ' '.join(''.join(alphabet_reverse[code] if code in alphabet_reverse else '' for code in word.split(' ')) for word in morse.split('  '))

morse = Morse()

# Príklady:
print(morse.encode('SOME TEXT HERE'))
# toto by mělo vrátit:
# ... --- -- .   - . -..- -   .... . .-. .

print(morse.decode('... --- -- .   - . -..- -   .... . .-. .'))
# Očakávaný výstup: SOME TEXT HERE

# Tajná zakódovaná správa:
print(morse.decode('-- .- .-. .-. -.--   -.-. .... .-. .. ... - -- .- ...   .- -. -..   .... .- .--. .--. -.--   -. . .--   -.-- . .- .-.'))