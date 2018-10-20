import tkinter
import re
from MorseCodes import codes

alpha_pattern = re.compile(r"[\w\.\,\:\;\?\-\_\(\)\=\+\/\@\' ]")
morse_pattern = re.compile(r"[·− \.\-]")
bin_pattern = re.compile(r"[01]")

def alpha_key(event):
    text = alpha_text.get("1.0", tkinter.END)
    new_text = ""
    new_binary = ""
    for character in text:
        if alpha_pattern.match(character):
            new_text += codes[character.upper()].code
            new_binary += codes[character.upper()].binary

    morse_text.delete("1.0", tkinter.END)
    morse_text.insert("1.0", new_text)

    bin_text.delete("1.0", tkinter.END)
    bin_text.insert("1.0", new_binary)

def morse_key(event):
    pass

def bin_key(event):
    pass

root = tkinter.Tk()

alpha_text = tkinter.Text(root, width=60, height=10)
morse_text = tkinter.Text(root, width=60, height=10)
bin_text = tkinter.Text(root, width=60, height=10)

alpha_text.bind_all("<Key>", alpha_key)
morse_text.bind_all("<Key>", morse_key)
bin_text.bind_all("<Key>", bin_key)

alpha_text.pack()
morse_text.pack()
bin_text.pack()
root.mainloop()