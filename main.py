print("Welcome to the Morse Code Converter! 😊")
print("  ~^~")
print(" (o.o) ")
print("  ( )  Let's convert your text into secret Morse code! 😎")
print("   U\n")

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Step 1: Get input from user
text = input("Enter the text you want to convert to Morse Code: ")


# Step 2: Covert text to Morse code using loop
def text_to_morse(txt):
    txt = txt.upper()
    morse_list = []

    for letter in txt:
        if letter in MORSE_CODE_DICT:
            morse_list.append(MORSE_CODE_DICT[letter])

    return ' '.join(morse_list)


morse = text_to_morse(txt=text)

print("\n✨✨✨ Here’s your Morse Code! ✨✨✨")
print("💻➡️ ", morse, "⬅️💻")
print("Thanks for using the Morse Code Converter! Have a great day! 🌟")
