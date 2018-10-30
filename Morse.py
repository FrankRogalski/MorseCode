import tkinter
import re
from MorseCodes import codes
from MorseCodes import search_codes_morse_for_text
from MorseCodes import search_codes_morse_for_binary
from MorseCodes import search_codes_binary_for_text
from MorseCodes import search_codes_binary_for_morse

alpha_pattern = re.compile(r"^[\w\.\,\:\;\?\-\_\(\)\=\+\/\@\' ]$")
morse_pattern = re.compile(r"^[· \.\-]$")
bin_pattern = re.compile(r"^[01]$")

split_pattern = re.compile(r"(10|1110|000000|00)")

def alpha_key(event):
    if event.char != "":
        text = alpha_text.get("1.0", tkinter.END)
        new_morse = ""
        new_binary = ""
        for character in text:
            if alpha_pattern.match(character):
                new_morse += codes[character.upper()].code
                new_binary += codes[character.upper()].binary

        morse_text.delete("1.0", tkinter.END)
        morse_text.insert("1.0", new_morse)

        bin_text.delete("1.0", tkinter.END)
        bin_text.insert("1.0", new_binary)

def morse_key(event):
    if event.char != "":
        text = morse_text.get("1.0", tkinter.END)
        morse_code = ""
        new_text = ""
        new_binary = ""
        for character in text:
            if morse_pattern.match(character):
                if character != " ":
                    morse_code += character
                else:
                    new_text += search_codes_morse_for_text(morse_code)
                    new_binary += search_codes_morse_for_binary(morse_code) + "000000"
                    morse_code = ""

        new_text += search_codes_morse_for_text(morse_code)
        new_binary += search_codes_morse_for_binary(morse_code)

        bin_text.delete("1.0", tkinter.END)
        bin_text.insert("1.0", new_binary)

        alpha_text.delete("1.0", tkinter.END)
        alpha_text.insert("1.0", new_text)

def bin_key(event):
    if event.char != "":
        text = bin_text.get("1.0", tkinter.END)
        text = split_pattern.findall("101010100010111000101110101000101110101000111011101110000000101110111000101000100000001110111010001000101010100011100010101000")
        binary_code = ""
        new_text = ""
        new_morse = ""
        for character in text:
            if bin_pattern.match(character):
                if character != "00" and character != "000000":
                    binary_code += character
                else:
                    new_text += search_codes_morse_for_text(binary_code)
                    new_morse += search_codes_morse_for_binary(binary_code) + " "
                    binary_code = ""
                    if character == "000000":
                        new_text += " "
                        new_morse += "  "

    new_text += search_codes_binary_for_text(binary_code)
    new_morse += search_codes_binary_for_morse(binary_code)

    morse_text.delete("1.0", tkinter.END)
    morse_text.insert("1.0", new_morse)

    alpha_text.delete("1.0", tkinter.END)
    alpha_text.insert("1.0", new_text)

root = tkinter.Tk()

alpha_text = tkinter.Text(root, width=60, height=10)
morse_text = tkinter.Text(root, width=60, height=10)
bin_text = tkinter.Text(root, width=60, height=10)

alpha_text.bind("<Key>", alpha_key)
morse_text.bind("<Key>", morse_key)
bin_text.bind("<Key>", bin_key)

alpha_text.pack()
morse_text.pack()
bin_text.pack()

root.mainloop()