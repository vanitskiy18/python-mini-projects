import random
from random import randint
from random import shuffle
from random import choice
print('Добро пожаловать в игру "Русская Рулетка"!\nПравила игры: Из мешка с пятью зелёными шариками и одним белым каждый игрок по очереди достаёт по одному шарику. Если достался зелёный шарик - игра идёт дальше, если кому-нибудь из игроков достался белый, то игра заканчивается, а если попадается оранжевый шарик, то игра (если игроков больше чем двое) продолжается, но игрок, которому попался оранжевый шарик, выбывает.\nПобеждает тот или те, кто не выбыл :)\nУдачи!')
players=[]
balls=[]
y=int(input('Введите количество всех шаров: '))
c=int(input('Введите количество оранжевых шаров: '))
for i in range(y):
    if i==c:
        marble='white'
    elif i<=c-1:
        marble='orange'
    else:
        marble='green'
    balls.append(marble)
random.shuffle(balls)    
players_counter=int(input('Введите количество игроков: '))
while players_counter==1:
    print('Нужно больше игроков!\nЗачем играть с самим собой?')
    players_counter=int(input('Введите количество игроков: '))
for a in range(players_counter):
    players.append(input(f'Введите имя игрока №{a+1}: '))
taken=1
current_player=0
chosen_marble=''
while taken<=y:
    x=input(f'Очередь игрока {players[current_player]}\nНажми Enter, чтобы достать шарик...')
    chosen_marble=random.choice(balls)
    balls.remove(chosen_marble)
    if chosen_marble=='white':
        print(f'Белый шарик!\nИгрок под именем {players[current_player]} проиграл\nИгра закончена.')
        break
    elif chosen_marble=='orange' and len(players)==2:
        print(f'Оранжевый шарик!\nИгрок под именем {players[current_player]} проиграл\nИгра закончена.')
        break
    elif chosen_marble=='orange':
        print(f'Оранжевый шарик!\nИгрок под именем {players[current_player]} проиграл, но игра продолжается!')
        players.remove(players[current_player])
    else:
        print('Всё хорошо, попался зелёный шарик.\nХод переходит к следующему игроку.')
    current_player=current_player+1
    if current_player>len(players)-1:
        current_player=0
    taken=taken+1
