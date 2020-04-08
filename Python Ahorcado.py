import random

# se define una constante con mayusculas 
IMAGES = ['''

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
   /    |
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


    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''


    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''


    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''


    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''

''']

WORD=['lavadora','secadora','sofa','democracia','diputado','teclado']


def main():
    word = random_word()
    hidden_word=['_']*len(word)  # uso de cadenas
    tries=0                      # intentos
    
    while True:
        show_board(hidden_word,tries)


def show_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('_.~"~._.~"~._.~"~._.~"~.~"~._.~"~._.~"~._.~"~._')



def random_word():
    idx = random.randint(0, len(WORD)-1)
    return WORD[idx]


if __name__ == '__main__':
    print('B I EN V E N I D O S  A L  J U E G O  A H O R C A D O S')
    main()