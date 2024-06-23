task = 'Практическое задание по уроку "Строки и индексация строк"'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
# 1. Задача
print('Введите слово:')
example = str(input())
length = int(len(example))
length1 = int(length // 2)
length2 = str(length)
length3 = length2[-1]
length4 = (int(length3))
print('Ваша фраза: ', example)
if length4 >= 2 and length4 <= 4 and length != 12:
    sim = 'а'
else:
    sim = 'ов'
if length == 1 or length == 21 or length == 31 or length == 41 or length == 51 or length == 61 or length == 71 or length == 81 or length == 91 or length == 101:
    sim = ' '
print()
print('Длина вашей фразы: ', length, ' символ' + sim)
print('Первый символ вашей фразы: ' + example[0])
print('Последний символ вашей фразы: ' + example[-1])
print('Первая половина символов вашей фразы: ' + example[:-length1])
print('Вторая половина символов вашей фразы: ' + example[length1:])
print('Обратный порядок вашей фразы: ' + example[::-1])
# a = example[::-2]
# print('Каждый второй символ вашей фразы: ' + a[::-1])
print('Каждый второй символ вашей фразы?: ' + example[1::2])
print()
print(thanks)