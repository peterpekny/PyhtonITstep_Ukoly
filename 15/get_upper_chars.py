def get_upper_chars(text):
    """ z textu vrací pouze znaky, které jsou velkými písmeny """
    """ např: Ahoj jsem teď v Praze -> vrátí pouze AP """
    
    upperchars = ''
    for char in text:
        if char.isupper():
            upperchars += ''.join(char)
    
    return upperchars