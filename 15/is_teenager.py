def is_teenager(age):
    """ vrací zda je teenager podle age """
    if age < 0:
        raise ValueError('Věk nemůže být záporný')
    return age >= 11 and age <= 19 # 11 - 19
