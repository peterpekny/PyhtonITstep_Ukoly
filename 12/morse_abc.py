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
    # Optimized by chat gpt
    def encode(self, text):
        # Zakoduje text 
        return '  '.join(' '.join(alphabet[char] for char in word) for word in text.upper().split(' '))

    def encode_old(self, text):
        
        encoded_message = []  

        # Prejde kazde slovo
        for word in text.upper().split(' '):
            encoded_word = []  

            # Prejde kazdy znak v slove
            for char in word:
                # ak existuje v dict
                if char in alphabet:
                    encoded_word.append(alphabet[char])
                # ak neexistuje pridam prazdny str
                else:
                    encoded_word.append('')  
                

            # pridam slovo do zpravy
            encoded_message.append(' '.join(encoded_word))

        # spoji slova
        return '  '.join(encoded_message)





    # Optimalizovane by chat GPT
    def decode(self, morse):
        #  Dekóduje morzeovú abecedu 
        return ' '.join(''.join(alphabet_reverse[code] if code in alphabet_reverse else '' for code in word.split(' ')) for word in morse.split('  '))

    def decode_old(self, morse):
        
        decoded_message = [] 

        # Prejdem kazde slovo (oddelene dvomi medzerami)
        for morse_word in morse.split('  '):
            decoded_word = [] 
            # prechadzam kazdy znak v slove
            for code in morse_word.split(' '):
                # Najde znak v slovniku alphabet_reverse, ak existuje
                if code in alphabet_reverse:
                    decoded_word.append(alphabet_reverse[code])
                else:
                    decoded_word.append('')  # ak nenajdem ziadny znak tak preskocim

            # Prida slovo do spravy
            decoded_message.append(''.join(decoded_word))

        # vrati zpravu
        return ' '.join(decoded_message)


morse = Morse()

# Príklady:
print(morse.encode('SOME TEXT HERE'))
print(morse.encode_old('SOME TEXT HERE'))
# toto by mělo vrátit:
# ... --- -- .   - . -..- -   .... . .-. .

print(morse.decode('... --- -- .   - . -..- -   .... . .-. .'))
print(morse.decode_old('... --- -- .   - . -..- -   .... . .-. .'))
# Očakávaný výstup: SOME TEXT HERE

# Tajná zakódovaná správa:
print(morse.decode('-- .- .-. .-. -.--   -.-. .... .-. .. ... - -- .- ...   .- -. -..   .... .- .--. .--. -.--   -. . .--   -.-- . .- .-.'))