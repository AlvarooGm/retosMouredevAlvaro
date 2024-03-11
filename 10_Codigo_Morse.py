'''

/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */

'''

morse_dict = {
    'A': '· —',
    'B': '— · · ·',
    'C': '— · — ·',
    'CH': '— — — —',
    'D': '— · ·',
    'E': '·',
    'F': '· · — ·',
    'G': '— — ·',
    'H': '· · · ·',
    'I': '· ·',
    'J': '· — — —',
    'K': '— · —',
    'L': '· — · ·',
    'M': '— —',
    'N': '— ·',
    'Ñ': '— — · — —',
    'O': '— — —',
    'P': '· — — ·',
    'Q': '— — · —',
    'R': '· — ·',
    'S': '· · ·',
    'T': '—',
    'U': '· · —',
    'V': '· · · —',
    'W': '· — —',
    'X': '— · · —',
    'Y': '— · — —',
    'Z': '— — · ·',
    '0': '— — — — —',
    '1': '· — — — —',
    '2': '· · — — —',
    '3': '· · · — —',
    '4': '· · · · —',
    '5': '· · · · ·',
    '6': '— · · · ·',
    '7': '— — · · ·',
    '8': '— — — · ·',
    '9': '— — — — ·',
    '.': '· — · — · —',
    ',': '— — · · — —',
    '?': '· · — — · ·',
    '"': '· — · · — ·'
}

palabra = input('Escriba la palabra a traducir: ').upper()
palCod = ''

for p in palabra:
    if p in morse_dict:
        palCod += morse_dict[p] + ' '
    else:
        palCod += ' '

print(palCod.strip())
