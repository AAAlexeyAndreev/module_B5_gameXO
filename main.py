import random

# Функция № 1 вывода игрового поля в консоль
def show_field_1(list_):
    for i in range(3):
        string = []
        for j in range(3):
            string.append(list_[6 - i * 3 + j])
        print(*string)

# Функция № 2 вывода игрового поля в консоль (просто аналог, чуть другая, можно и одной обойтись)
def show_field_2(list_):
    for i in range(3):
        string = ''
        for j in range(3):
            string = string + str(list_[6 - i * 3 + j]) + ' '
        print(string)

''' Функция запроса символа от игрока
Счётчик считает количество неправильных вводов. В зависимости от количества неправильных
вводов функция комментирует действия игрока. 
'''
def funct_input(set_arg):
    attempt_count=0
    comments = ('Читать не умеешь? ', 'Просто цифру надо нажать. ', 'Уф ... ',
                'Это тебе надо. ', 'Иди, что-ли, в мячик поиграй. ', 'Я так долго могу. ',
                'Займись делом. ', 'Тру-ля-ля. ', 'Может тебе анекдот рассказать? ',
                'Взрослый человек вроде. ', 'На что я трачу свой время. ', 'Как же мне это надоело. ',
                'Сделай уже ход. ', 'Ты не только мёртвого, ты и машину достанешь. ')
    while True:
        s = input('Введи цифру из второго поля, куда хочешь сделать ход: ')
        if s in set_arg:
            return s
        elif attempt_count <= 10:
            attempt_count += 1
        elif 10 < attempt_count <= 15:
            attempt_count += 1
            print('Ну давай же.')
        elif attempt_count <= 100:
            print(random.choice(comments))
            attempt_count += 1
        else:
            print('Спать я пошёл.')
            return None

# Функция для контроля побед
def winner_user(set_1, set_2):
    win_combinations = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},
                       {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
                       {1, 5, 9}, {3, 5, 7}]
    for set_k in win_combinations:
        if set_k.intersection(set_1) == set_k or len(set_k.intersection(set_2)) == 3:
            return True

    return False

#Основное игровое поле'
game_field = ['■'] * 9

#Контрольное поле
control_field = []
for i in range(9):
    control_field.append(str(i+1))

# Множество для контроля повторных ходов
control_set = set(control_field)
# Множества для контроля победы
set_x = set()
set_0 = set()


show_field_1(game_field)
print()
show_field_2(control_field)

# Игра
for i in range(9):

    if not i % 2:
        print('Ходит крестик (Х)')
    else:
        print('Ходит нолик (0)')

    z = funct_input(control_set)
    if z is None: break

    if not i % 2:
        game_field[(int(z)-1)] = 'X'
        set_x.add(int(z))
    else:
        game_field[(int(z)-1)] = '0'
        set_0.add(int(z))
    control_field[(int(z)-1)] = ' '
    control_set.discard(z)

    show_field_1(game_field)
    print('-'*5)
    print('Нажмите одну из цифр для хода:')
    show_field_2(control_field)

    if winner_user(set_x, set_0) is True:
        show_field_1(game_field)
        print('Победили', game_field[(int(z)-1)])
        break


if winner_user(set_x, set_0) is False:
    print('Ничья, попробуйте ещё раз')