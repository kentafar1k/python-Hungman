from random import *
words_list2 = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие", "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин", "председатель", "сотрудник", "республика", "личность"]
words_list = ["человек", "слово"]
def get_word():
    return choice(words_list)
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
word = get_word()
def play(word):
    tries = 6
    wor = ['_' for i in range(len(word))]
    flag = True
    while tries != -1:
        if ''.join(wor) == word:
            flag = True
            break
        guess = input('Угадай букву: ')
        indices = [i for i in range(len(word)) if word[i] == guess]
        if guess in word:
            for index in indices:
                wor[index] = guess
            print('Такая буква есть, молодец!')
            print(''.join(wor))
        else:
            print('Такой буквы нету')
            print(display_hangman(tries))
            tries -= 1
            flag = False
    if flag:
        print('ультрамегахарош')
    else:
        print('ты проиграл')



play(word)