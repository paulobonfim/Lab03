# Import:
import random

lst = ['''

>>>>>>>>>>>>>>Hangman<<<<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

+----+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

+----+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

+----+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Forca:
    def __init__(self, palavra, count=0):
        self.palavra = palavra
        self.count = count
        print("Hangman")
        print(lst[0])

    def comecar(self, a):
        self.a = a
        b = len(a)
        letreiro = ("-") * b
        c = list(letreiro)
        print("Palavras: ", letreiro)
        print("Letras corretas: ")
        print("Letras erradas: ")
        correta = "\n"
        errada = "\n"
        counter = b
        while counter > 0 and self.count < 6:
            letra = input("digite: ")
            if letra in a:
                u = a.index(letra)
                c[u] = letra
                correta = correta + letra + "\n"
                counter = counter - 1
            else:
                self.count += 1
                errada = errada + letra + '\n'

            print(lst[self.count])
            print("Palavra: ", "".join(c))
            print("Letra errada:", errada)
            print("Letra correta:", correta)

    def verifica(self):
        if self.count == 6:
            print("Game over. Tente outra vez")
        else:
            print("Parabéns, você venceu!!!!")

def escolha():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
        return bank[random.randint(0, len(bank))].strip()

def main():
    game = Forca(escolha())
    game.comecar(escolha())
    game.verifica()

if __name__ == "__main__":
    main()
