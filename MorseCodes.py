from CodeTranslations import Morse

codes = {
    "A": Morse("·−"),
    "B": Morse("−···"),
    "C": Morse("−·−·"),
    "D": Morse("−··"),
    "E": Morse("·"),
    "F": Morse("··−·"),
    "G": Morse("−−·"),
    "H": Morse("····"),
    "I": Morse("··"),
    "J": Morse("·−−−"),
    "K": Morse("−·−"),
    "L": Morse("·−··"),
    "M": Morse("−−"),
    "N": Morse("−·"),
    "O": Morse("−−−"),
    "P": Morse("·−−·"),
    "Q": Morse("−−·−"),
    "R": Morse("·−·"),
    "S": Morse("···"),
    "T": Morse("−"),
    "U": Morse("··−"),
    "V": Morse("···−"),
    "W": Morse("·−−"),
    "X": Morse("−··−"),
    "Y": Morse("−·−−"),
    "Z": Morse("−−··"),

    "1": Morse("·−−−−"),
    "2": Morse("··−−−"),
    "3": Morse("···−−"),
    "4": Morse("····−"),
    "5": Morse("·····"),
    "6": Morse("−····"),
    "7": Morse("−−···"),
    "8": Morse("−−−··"),
    "9": Morse("−−−−·"),
    "0": Morse("−−−−−"),
    
    "Å": Morse("·−−·−"),
    "À": Morse("·−−·−"),
    "Ä": Morse("·−·−"),
    "È": Morse("·−··−"),
    "É": Morse("··−··"),
    "Ö": Morse("−−−·"),
    "Ü": Morse("··−−"),
    "SS": Morse("···−−··"), #ß
    "Ñ": Morse("−−·−−"),
    ".": Morse("·−·−·−"),
    ",": Morse("−−··−−"),
    ":": Morse("−−−···"),
    ";": Morse("−·−·−·"),
    "?": Morse("··−−··"),
    "-": Morse("−····−"),
    "_": Morse("··−−·−"),
    "(": Morse("−·−−·"),
    ")": Morse("−·−−·−"),
    "'": Morse("·−−−−·"),
    "=": Morse("−···−"),
    "+": Morse("·−·−·"),
    "/": Morse("−··−·"),
    "@": Morse("·−−·−·"),

    " ": Morse(" ")
}

def search_codes_morse_for_text(search_term):
    if type(search_term) != "string":
        return ""
    for k in codes:
        if codes[k].code == search_term:
            return k
    return ""

def search_codes_morse_for_binary(search_term):
    if type(search_term) != "string":
        return ""
    for k in codes:
        if codes[k].code == search_term:
            return codes[k].binary
    return ""