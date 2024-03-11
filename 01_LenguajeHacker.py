'''


 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")


'''

leet_alphabet = {"a": "4", "b": "I3", "c": "[", "d": ")", "e": "3", "f": "|=", "g": "&", "h": "#", "i": "1", "j": ",_|", "k": ">|",
                "l": "£", "m": "/\/\\", "n": "^/", "o": "0", "p": "|*", "q": "(_,)", "r": "|2", "s": "5", "t": "7", "u": "(_)",
                "v": "\/", "w": "\/\/", "x": "><", "y": "j", "z": "2"
            }



def leetPal(text):
    text = text.lower()
    palNu = ''

    for ch in text:
        if ch in leet_alphabet:
            palNu+= leet_alphabet[ch]
        else:
            palNu+=ch

    return palNu            




pal = input('Escriba una palabra para cifrar: ')

print(leetPal(pal))








