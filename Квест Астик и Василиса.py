
from random import randint
class Monsters():
    def __init__(self,name, hp, weapon,attack):
        self.name = name
        self.hp = hp
        self.attack = randint(1,3)
        self.weapon = str(weapon)
    def print_info(self):
        print(self.name,'один из самых слабых монстров, так что ты сможешь с легкостью его одалеть!')
        print('Oружие:',self.weapon)
        print('Очки здоровья:', self.hp)
        print('Сила аттаки:', self.attack)

    def attack(self, warrior):
        print(self.name, 'стреляет слизью в', warrior.name)
        print('Результат схватки для', self.name)
        self.print_info()
        print('Результат схватки для', warrior.name)
        warrior.print_info()
class Hero():
    def __init__(self, nickname, hp, weapon, attack):
        self.nickname = nickname
        self.hp = 20
        self.attack = randint(2, 8)
        self.weapon = str(weapon)
    def print_info(self):
        print('Имя:', self.nickname)
        print('Твое оружие:', self.weapon)
        print('Очки здоровья:', self.hp)
        print('Сила аттаки:', self.attack)
def menu_fight():
    while slaim.hp > 0:
        print('Вы hp:',warrior.hp,'attack:',warrior.attack)
        print('Враг hp:',slaim.hp,'attack:',slaim.attack)
        print("**********************")
        print("1)Ударить")
        print("2)Хил 0-5")
        n = input("Введите число: ")
        if n == 1:
            # Здоровье врага отнимает от вашего дамага.
            slaim.hp -= warrior.attack
            print("Вы ударили противника, у него осталось hp:",slaim.hp)
            # Здоровье игрока отнимает от дамага врага.
            warrior.hp -= slaim.attack
            print("Противник ударил вас, у вас осталось %s hp:", warrior.hp)

            print("*********************")

        if n == 2:
            # Рандомно от 0 до 5 добавляет хп.
            p.hp += randint(0,5)
            # Если здоровье игрока больше, то хп игрока будет равна 100.
            if p.hp > 100:
                p.hp = 100

            print("Ваши хп:",p.hp)

        else:
             print("Чего ждем?")
        if p.hp < 0:
            print("Вы проиграли")
        if e.hp < 0:
            print("Вы победили")

        print("******************")
print("Достаточно ли вы храбры, чтобы начать игру?!(Да/Нет)")
ready = input().lower()
while ready!='да':
    if ready == "да":
        print ("Прекрасно,тогда мы начинаем!")
    elif ready == "нет":
        print ("Ты не хочешь преключения?У нас тут весело.....Увидимся в следующий раз!")
        print('Может быть передумал?')
        ready = input().lower()
    else:
        print ("Я не понимаю")
        print("Достаточно ли вы храбры, чтобы начать игру?!(Да/Нет)")
        ready = input().lower()
print("Прекрасно,тогда мы начинаем!")
print('**************************************************************************************************************************')
print('Привет славный герой!Ты появился в волщебном мире.Тебе предется одолеть дракона, чтобы спасти принцессу от страшной участи')
print('**************************************************************************************************************************')
print('Назови свое гордое имя герой!')
name = input()
print('Славное имя,',name,',тепрь тебе предстоит сразится с чудовищами и разбойниками, чтоб стать сильнее и освободить прекрасную принцессу из лап дракона!')
warrior = Hero(name, "20", "Меч",'2-8')
warrior.print_info()
print('****************************************************************************************************************************************')
print('Первый монстор, которого придется тебе одолеть - это Слайм.')
slaim = Monsters('Cлайм','8','Слизь','1-3')
slaim.print_info()
print('Хотите увидеть еще раз вашу и врага статистику?(Да/Нет)')
stats =input().lower()
if stats == "да":
    print('Вы:', warrior.print_info())
    print('Враг:', slaim.print_info())
if stats == "нет":
    print('Начать сражение?(Да/Нет)')
else:
    print('Начать сражение?(Да/Нет)')
start = input().lower()
if start == 'да':
   menu_fight()
print('---')

if start == 'нет':
    print("Не победив его, ты не станешь сильнее")
    print('Начать сражение?(Да/Нет)')
    start = input().lower()
else:
    print('Я не понимаю чего ты хочешь.')
    print('Начать сражение?(Да/Нет)')
    start = input().lower()