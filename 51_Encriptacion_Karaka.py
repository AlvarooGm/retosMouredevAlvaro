'''

/*
 * Crea una función que sea capaz de encriptar y desencriptar texto
 * utilizando el algoritmo de encriptación de Karaca
 * (debes buscar información sobre él).
 */

Make a function that encrypts a given input with these steps:
Input: “apple”
Step 1: Reverse the input: “elppa”
Step 2: Replace all vowels using the following chart:
a => 0, e => 1, i => 2, o => 3, u => 4 # “1lpp0”
Step 3: Add “aca” to the end of the word: “1lpp0aca”
Output: “1lpp0aca”
All inputs are strings, no uppercases and all output must be strings.

'''

palabra = 'apple'
palabra = palabra[::-1]

for l in palabra:
    if l == 'a':
        palabra = palabra.replace(l,'0')
    if l == 'e':
        palabra = palabra.replace(l,'1')
    if l == 'i':
        palabra = palabra.replace(l,'2')
    if l == 'o':
        palabra = palabra.replace(l,'3')
    if l == 'u':
        palabra = palabra.replace(l,'4')
     

print(palabra+'aca')


