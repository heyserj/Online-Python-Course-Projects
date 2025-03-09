CONVERSION_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "(": "-.--.",
    "-": "-....-",
    "&": ".-...",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    ")": "-.--.-",
    ":": "---...",
    "!": "-.-.--",
    "$": "...-..-",
    ";": "-.-.-.",
    "/": "-..-.",
    "=": "-...-",
    "@": ".--.-.",
    '"': ".-..-.",
    ".": ".-.-.-",
    "+": ".-.-.",
    "_": "..--.-"
}

def text_to_morse_code(text):
    """Takes a plain-text string as input and converts it to morse code. Returns the converted string."""
    
    converted_text = ""

    # loop through each character in the input
    for char in text:
        if char == " ":
            converted_text = converted_text[:-1] + "/"
        else:
            morse_code_equivalent = CONVERSION_DICT[char]
            converted_text += f"{morse_code_equivalent} "
    
    return converted_text


while True:
    # prompt the user for input
    plain_text = input("Please enter the text you'd like to convert to morse code or enter 'q' to quit.\n").upper()
    if plain_text == "Q":
        break

    try:
        converted_text = text_to_morse_code(plain_text)
    except KeyError as e:
        print("You entered an invalid character. Please try again.\n")
    else:
        print(f"The converted text is {converted_text}\n")
