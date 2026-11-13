from itertools import permutations

alphabet = ''.join(list(map(str, input('Введите цифры через пробел:').split())))
count = int(input('Введите длину перестановки:'))

def perm_to_num(alph, cnt, nd):
    combinations = []
    cntr = 0
    for w in permutations(sorted(alph), cnt):
        word = ''.join(sorted(w))
        if word not in combinations:
            if word == nd:
                return(cntr)
            combinations.append(word)
            cntr += 1
    return -1

def num_to_perm(alph, cnt, nd):
    combinations = []
    cntr = 0
    for w in permutations(sorted(alph), cnt):
        word = ''.join(sorted(w))
        if word not in combinations:
            if cntr == nd:
                return(word)
            combinations.append(word)
            cntr += 1
    return -1

print('Чтобы выбрать функцию, введите номер: 1-узнать номер перестановки, 2-узнать перестановку по номеру')
func = int(input('Выберите функцию:'))

if func == 1:
    needed = str(input('Введите перестановку(в порядке возрастания цифр), номер которой хотите узнать:'))
    res = perm_to_num(alphabet, count, needed)
    if res == -1:
        print('Такой перестановки нет :(')
    else:
        print(f'Результат:{res}')

if func == 2:
    needed = int(input('Введите номер, перестановку которого хотите узнать:'))
    res = num_to_perm(alphabet, count, needed)
    if res == -1:
        print('Такой перестановки нет :(')
    else:
        print(f'Результат:{res}')
