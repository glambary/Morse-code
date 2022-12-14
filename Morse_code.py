import random

answer = []
words = ['code', 'bit', 'list', 'soul', 'horse', 'stone', 'sleep', 'dream', 'program', 'python', 'team']


def main():
    print('Добро пожаловать в игру!')
    user_name = input('Введите имя\n')
    print(f'''Привет, {user_name}!
Все слова, используемые в данной игре, состоят исключительно из букв латинского алфавита.
Нажмите Enter и начнём.''')
    input()

    counter = 1
    while words:
        random_word = get_word()
        print(f'Слово {counter} {morse_encode(random_word)}')
        user_word = input().lower()
        if user_word == 'stop':
            break
        if random_word == user_word:
            answer.append(True)
            print(f'Верно, {user_name}!')
        else:
            answer.append(False)
            print(f'Неверно, {user_name}!')
        counter += 1
    print(f'''Игра закончена!
    Всего задачек: {len(answer)}
    Отвечено верно: {answer.count(True)}
    Отвечено неверно: {answer.count(False)}''')


def morse_encode(word):
    """
    Эта функция преобразует слово в код Морзе.

    Пример:
        Входной параметр(type str, только латинские буквы): get
        Возвращаемое значение(type str): −−. . −
    """
    code = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
    }
    word = list(word)
    for i in range(len(word)):
        word[i] = code.get(word[i], 0)
    return ' '.join(word)


def get_word():
    """
    Возвращает рандомно выбранное слово (type str) из списка words
    """
    global words
    word = random.choice(words)
    words.remove(word)
    return word


main()

