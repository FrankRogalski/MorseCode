class Morse:
    def __init__(self, code):
        self.code = code + " "
        binary = ""
        for char in self.code:
            if char == "·":
                binary += "10"
            elif char == "−":
                binary += "1110"
            elif char == " ":
                binary += "00"

        self.binary = binary