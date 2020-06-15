phrase = input("Ingresa tu frase:  \n"  )

def palindrome (phrase):
    phrase = phrase.replace(" ","")
    phrase = phrase.casefold()

    if phrase == phrase[::-1]:
        print(f' {phrase} es un palíndromo')
    else:
        print(f' {phrase} no es un palíndromo')

palindrome(phrase)