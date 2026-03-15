import random
i=0
a=[]
class Player:
    def __init__(self,nickname):
        self.nickname=nickname
    def get_color(self):
        return self.set_color()
    def set_color(self):
        if len(colors)>0:
            x=' '.join(colors)
            print(f'Выберите цвет: {x}')
            y=input('Введите цвет: ')
            if y in colors:
                self.color=y
                print(f'Выбран цвет: {y}')
                colors.remove(y)
            else:
                print('Такого цвета нет! Выберите другой.')
        elif len(colors)==0:
            print('Цвет не может быть назначен! Очередь уже заполнена):')
    def get_role(self):
        return self.set_role()
    def set_role(self):
        global i,a
        if len(a)==len(roles):
            print('Роль не может быть назначена! Очередь уже заполнена):')
        elif len(a)+1==len(roles) and not 'imposter' in a:
            role='imposter'
            self.role=role
            a.append(role)
            print(f'{self.nickname} is imposter')
        elif random.choice(roles)==0 and len(a)<len(roles):
            if i==1:
                role='not imposter'
                self.role=role
                a.append(role)
                print(f'{self.nickname} is not imposter')
            elif i==0:
                role='imposter'
                a.append(role)
                self.role=role
                print(f'{self.nickname} is imposter')
                i=i+1
        elif random.choice(roles)!=0 and len(a)<len(roles):   
            role='not imposter'
            self.role=role
            a.append(role)
            print(f'{self.nickname} is not imposter')
player1=Player('Alice558')
player2=Player('Mike557')
player3=Player('LonelyMan556')
player4=Player('LonelyMan557')
colors=['red','green','blue']
player1.set_color()
player2.set_color()
player3.set_color()
player4.set_color()
roles=[0,1,2]
player1.set_role()
player2.set_role()
player3.set_role()
player4.set_role()
