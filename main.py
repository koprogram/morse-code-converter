# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

# Function to convert text to Morse code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char not in MORSE_CODE_DICT:
            return "Error: Character '{}' cannot be translated to Morse Code!".format(char)
        morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code.strip()

# Function to convert Morse code to text
def morse_to_text(morse_code):
    morse_to_text_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    text = ''
    for code in morse_code.split(' '):
        if code == '/':
            text += ' '
        elif code in morse_to_text_dict:
            text += morse_to_text_dict[code]
        else:
            return "Error: Morse code '{}' cannot be translated to text!".format(code)
    return text

# Main program loop
def main():
    while True:
        mode = input("Enter 'T' to convert Text to Morse Code or 'M' to convert Morse Code to Text (or 'Q' to Quit): ").upper()
        if mode == 'T':
            text = input("Enter text to convert to Morse Code: ")
            result = text_to_morse(text)
            print("Morse Code:", result)
        elif mode == 'M':
            morse_code = input("Enter Morse Code to convert to Text (use '/' for space): ")
            result = morse_to_text(morse_code)
            print("Text:", result)
        elif mode == 'Q':
            print("Exiting the Morse Code Converter.")
            break
        else:
            print("Invalid mode selected. Please enter 'T' for Text to Morse, 'M' for Morse to Text, or 'Q' to Quit.")
        print()  # Print a blank line for cleaner output spacing

if __name__ == "__main__":
    main()
