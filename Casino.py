from decouple import config
from start_game import game

My_money = config('My_Money', cast=int)
while True:
    print(f'\nВ моём кошельке {My_money}$')
    print('Хотите сыргать в рулетку ? (y/n)')
    answer = input('')
    if answer == 'n':
        print('Наше дело предложить. Всего вам доброго.')
        break
    elif My_money == 0:
        print(f'У вас не осталось денег')
        break
    elif answer == 'y':
        print('Отлично, мы наченаем!')
        ctavka = int(input('Ваша сумма ставки: '))
        vybor = int(input('Выберите цифру от 1 до 30:'))
        print('Ставки сделанны, ставок больше нет.')
        My_money -= ctavka
        My_money += game(vybor, ctavka)
        print(f'В кармане {My_money}$')
        continue
    else:
        print('Вы не правельно поняли.')
