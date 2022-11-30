from random import randint
import time


def game(vybor, ctavka):
    while True:
        print('--------------Барабан крутится, денги мутятся----------')
        time.sleep(4)
        choice = randint(1, 31)
        if choice == vybor:
            print(f'------{choice}------')
            print('Наши поздравлении, вы выйграли!')
            return ctavka * 2
        else:
            print(f'\n-------------Выпал сектор {choice}------------')
            print(f'Ваша сумма  проигрыша {ctavka}$')
            print('Очень жаль, Повезёт в другой раз.')
            return 0





