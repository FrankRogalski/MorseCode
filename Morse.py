import tkinter
import re
from MorseCodes import codes
from MorseCodes import search_codes_morse_for_text
from MorseCodes import search_codes_morse_for_binary

alpha_pattern = re.compile(r"^[\w\.\,\:\;\?\-\_\(\)\=\+\/\@\' ]$")
morse_pattern = re.compile(r"^[· \.\-]$")
bin_pattern = re.compile(r"^[01]$")

def alpha_key(event):
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
    text = morse_text.get("1.0", tkinter.END)
    char = ""
    new_text = ""
    new_binary = ""
    for character in text:
        if morse_pattern.match(character):
            if character != " ":
                char += character
            else:
                new_text += search_codes_morse_for_text(char)
                new_binary += search_codes_morse_for_binary(char)
                char = ""

    new_text += search_codes_morse_for_text(char)
    new_binary += search_codes_morse_for_binary(char)

    bin_text.delete("1.0", tkinter.END)
    bin_text.insert("1.0", new_binary)

    alpha_text.delete("1.0", tkinter.END)
    alpha_text.insert("1.0", new_text)


def bin_key(event):
    pass

root = tkinter.Tk()

alpha_text = tkinter.Text(root, width=60, height=10)
morse_text = tkinter.Text(root, width=60, height=10)
bin_text = tkinter.Text(root, width=60, height=10)

alpha_text.bind_all("<Key>", alpha_key)
morse_text.bind("<Key>", morse_key)
bin_text.bind("<Key>", bin_key)

alpha_text.pack()
morse_text.pack()
bin_text.pack()

root.mainloop()