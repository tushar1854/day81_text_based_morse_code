MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', " ": "/"}


def string_to_mor(string):
    new_str = ""
    for alp in string:
        new_str += MORSE_CODE_DICT[alp]
        new_str += " "
    return new_str


def mor_to_string(mor_code):
    new_str = ""
    mor_lst = mor_code.split(" ")
    for code in mor_lst:
        for d_alp, d_code in MORSE_CODE_DICT.items():
            if d_code == code:
                new_str += d_alp
    return new_str


choice = input('What you will write for "morse_code":m or "string":s ')
if choice == "m":
    mor_code = (input("Enter the word "))
    print(mor_to_string(mor_code))
elif choice == "s":
    string = (input("Enter the word ")).upper()
    print(string_to_mor(string))
else:
    print("Please check your spelling")
