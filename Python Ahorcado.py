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
        # Mostrar el tablero
        show_board(hidden_word,tries)
        current_letter =str(input('Escoge una letra: '))
        current_letter = current_letter.lower()

        # Logica
        letter_indexes=[]
        for  idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        
        if(len(letter_indexes))==0: # si la lista esta vacia no fue correcto
            tries += 1
            if tries== 7:
                show_board(hidden_word, tries)
                print('')
                print('')
                print('Perdiste, La palabra correcta era {}'.format(word))
                break
        else:                       # si la lista tiene algo se cambia el _ por la letra digitada
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes =[]

        try:
            hidden_word.index('_')
        except ValueError:
            print('')
            print('GANASTE, Felicidades!. La palabra es {}'.format(word))
            break
        


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