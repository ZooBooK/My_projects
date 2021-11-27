# Игра крестики нолики 28.11.2021
# Основыне условия - Очередь первого хода / Словарь с игровым полем
whose_move = ' x '
d_2 = {'p1':' 1 ', 'p2' : ' 2 ', 'p3' : ' 3 ', 'p4' : ' 4 ', 'p5' : ' 5 ', 'p6' : ' 6 ', 'p7' : ' 7 ', 'p8':' 8 ', 'p9' : ' 9 '}

# Условия для проверки победных комбинаций
while (' x ' not in d_2['p1'] or ' x ' not in d_2['p2'] or ' x ' not in d_2['p3']) and (' x ' not in d_2['p4'] or ' x ' not in d_2['p5'] or ' x ' not in d_2['p6'])\
    and (' x ' not in d_2['p7'] or ' x ' not in d_2['p8'] or ' x ' not in d_2['p9']) and (' x ' not in d_2['p1'] or ' x ' not in d_2['p5'] or ' x ' not in d_2['p9'])\
    and (' x ' not in d_2['p3'] or ' x ' not in d_2['p5'] or ' x ' not in d_2['p7']) and (' x ' not in d_2['p1'] or ' x ' not in d_2['p4'] or ' x ' not in d_2['p7'])\
    and (' x ' not in d_2['p2'] or ' x ' not in d_2['p5'] or ' x ' not in d_2['p8']) and (' x ' not in d_2['p3'] or ' x ' not in d_2['p6'] or ' x ' not in d_2['p9'])\
    and (' 0 ' not in d_2['p1'] or ' 0 ' not in d_2['p2'] or ' 0 ' not in d_2['p3']) and (' 0 ' not in d_2['p4'] or ' 0 ' not in d_2['p5'] or ' 0 ' not in d_2['p6'])\
    and (' 0 ' not in d_2['p7'] or ' 0 ' not in d_2['p8'] or ' 0 ' not in d_2['p9']) and (' 0 ' not in d_2['p1'] or ' 0 ' not in d_2['p5'] or ' 0 ' not in d_2['p9'])\
    and (' 0 ' not in d_2['p3'] or ' 0 ' not in d_2['p5'] or ' 0 ' not in d_2['p7']) and (' 0 ' not in d_2['p1'] or ' 0 ' not in d_2['p4'] or ' 0 ' not in d_2['p9'])\
    and (' 0 ' not in d_2['p2'] or ' 0 ' not in d_2['p5'] or ' 0 ' not in d_2['p8']) and (' 0 ' not in d_2['p3'] or ' 0 ' not in d_2['p6'] or ' 0 ' not in d_2['p9']):
    # Распечатка игрового поля
    print('\n')
    print('Это ваше игровое поле: ')
    print('\n',d_2['p1'],d_2['p2'],d_2['p3'],'\n',d_2['p4'],d_2['p5'],d_2['p6'],'\n',d_2['p7'],d_2['p8'],d_2['p9'])

    print('\n')

    # Очередь хода
    if whose_move == ' x ':
        location_move_X = input('Ход "X", введите цифру соответствующую позиции, куда вы хотите сходить:  ')
    if whose_move == ' x ':
        whose_move = ' 0 '
        # Условия для крестиков
        if location_move_X == '1':
            d_2['p1'] = ' x '
        if location_move_X == '2':
            d_2['p2'] = ' x '
        if location_move_X == '3':
            d_2['p3'] = ' x '
        if location_move_X == '4':
            d_2['p4'] = ' x '
        if location_move_X == '5':
            d_2['p5'] = ' x '
        if location_move_X == '6':
            d_2['p6'] = ' x '
        if location_move_X == '7':
            d_2['p7'] = ' x '
        if location_move_X == '8':
            d_2['p8'] = ' x '
        if location_move_X == '9':
            d_2['p9'] = ' x '
    # Распечатка игрового поля
    print('\n')
    print('Это ваше игровое поле: ')
    print('\n', d_2['p1'], d_2['p2'], d_2['p3'], '\n', d_2['p4'], d_2['p5'], d_2['p6'], '\n', d_2['p7'], d_2['p8'], d_2['p9'])
    
    print('\n')

    # Смена череды хода
    if whose_move == ' 0 ':
        location_move_0 = input('Ход "0", введите цифру соответствующую позиции, куда вы хотите сходить:  ')
        if whose_move == ' 0 ':
            whose_move = ' x '
        # Условия для ноликов
        if location_move_0 == '1':
            d_2['p1'] = ' 0 '
        if location_move_0 == '2':
            d_2['p2'] = ' 0 '
        if location_move_0 == '3':
            d_2['p3'] = ' 0 '
        if location_move_0 == '4':
            d_2['p4'] = ' 0 '
        if location_move_0 == '5':
            d_2['p5'] = ' 0 '
        if location_move_0 == '6':
            d_2['p6'] = ' 0 '
        if location_move_0 == '7':
            d_2['p7'] = ' 0 '
        if location_move_0 == '8':
            d_2['p8'] = ' 0 '
        if location_move_0 == '9':
            d_2['p9'] = ' 0 '

# Проверка какой игрок выиграл
# Проверка условий победы "Ноликов"
else:
    if d_2['p1'] == ' x ' and d_2['p2'] == ' x ' and d_2['p3'] == ' x ' or d_2['p4'] == ' x ' and d_2['p5'] == ' x ' and d_2['p6'] == ' x '\
    or d_2['p7'] == ' x ' and d_2['p8'] == ' x ' and d_2['p9'] == ' x ' or d_2['p1'] == ' x ' and d_2['p5'] == ' x ' and d_2['p9'] == ' x '\
    or d_2['p3'] == ' x ' and d_2['p5'] == ' x ' and d_2['p7'] == ' x ' or d_2['p1'] == ' x ' and d_2['p4'] == ' x ' and d_2['p7'] == ' x '\
    or d_2['p2'] == ' x ' and d_2['p5'] == ' x ' and d_2['p8'] == ' x ' or d_2['p3'] == ' x ' and d_2['p6'] == ' x ' and d_2['p9'] == ' x ':
        # Вывод итогового поля / победителя
        print('\n', d_2['p1'], d_2['p2'], d_2['p3'], '\n', d_2['p4'], d_2['p5'], d_2['p6'], '\n', d_2['p7'],d_2['p8'], d_2['p9'])
        print('крестики победили')

    # Проверка условий победы "Ноликов"
    else:
        if d_2['p1'] == ' 0 ' and d_2['p2'] == ' 0 ' and d_2['p3'] == ' 0 ' or d_2['p4'] == ' 0 ' and d_2['p5'] == ' 0 ' and d_2['p6'] == ' 0 '\
        or d_2['p7'] == ' 0 ' and d_2['p8'] == ' 0 ' and d_2['p9'] == ' 0 ' or d_2['p1'] == ' 0 ' and d_2['p5'] == ' 0 ' and d_2['p9'] == ' 0 '\
        or d_2['p3'] == ' 0 ' and d_2['p5'] == ' 0 ' and d_2['p7'] == ' 0 ' or d_2['p1'] == ' 0 ' and d_2['p4'] == ' 0 ' and d_2['p7'] == ' 0 '\
        or d_2['p2'] == ' 0 ' and d_2['p5'] == ' 0 ' and d_2['p8'] == ' 0 ' or d_2['p3'] == ' 0 ' and d_2['p6'] == ' 0 ' and d_2['p9'] == ' 0 ':
            # Вывод итогового поля / победителя
            print('\n', d_2['p1'], d_2['p2'], d_2['p3'], '\n', d_2['p4'], d_2['p5'], d_2['p6'], '\n', d_2['p7'],d_2['p8'], d_2['p9'])
            print('Нолики победили')