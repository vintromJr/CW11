import random

warrior_list = ['Доброволець', 'Нацгвардієць', 'Вояк ЗСУ', 'Спецназовець']
enemy_list = ['Москаль', 'Бурят', 'Кадировець', 'Сепаратист']
arm_list = [['Пістолет', 10], ['Автомат', 20], ['Кулемет', 30], ['РПГ', 40], ['Джавелін', 50]]
defence_list = [['Без захисту', 0], ['Шолом', 10], ['Бронежилет', 20]]

class Power:
    def __init__(self):
        super().__init__()
        self.power = random.randint(7,12) * 10

class Enemy(Power):
    def __init__(self):
        super().__init__()
        self.enemy = enemy_list[random.randint(0,3)]

class Me(Power):
    def __init__(self, name, age):
        super().__init__()
        self.__my_name = warrior_list[random.randint(0,3)] + ' ' + name
        self.__my_enemy = Enemy()
        if 18 <= age <= 60: self.__age = age
        else: self.__age = 18
        print('Суперники:')
        print("%s (%s років)" % (self.__my_name, self.__age), 'з початковою міццю:', str(self.power))
        print(self.__my_enemy.enemy, 'з початковою міццю:', str(self.__my_enemy.power))
        print()
        print('*' * 30)
        print()

    def fight(self, num):
        print('Бій %s відбувся:' % num)
        rand1 = arm_list[random.randint(0,4)]
        rand2 = defence_list[random.randint(0, 2)]
        pow1 = rand1[1] + rand2[1]
        self.power += pow1
        self.__my_enemy.power -= pow1
        print(self.__my_name + ':')
        print('\t' + 'Зброя: ' + rand1[0])
        print('\t' + 'Захист: ' + rand2[0])
        rand1 = arm_list[random.randint(0, 4)]
        rand2 = defence_list[random.randint(0, 2)]
        pow2 = rand1[1] + rand2[1]
        self.power -= pow2
        self.__my_enemy.power += pow2
        print('\t' + 'Міць: ' + str(self.power))
        print(self.__my_enemy.enemy + ':')
        print('\t' + 'Зброя: ' + rand1[0])
        print('\t' + 'Захист: ' + rand2[0])
        print('\t' + 'Міць: ' + str(self.__my_enemy.power))
        if pow1 > pow2: print('Переміг: ' + self.__my_name)
        elif pow1 < pow2: print('Переміг: ' + self.__my_enemy.enemy)
        else: print('Нічия')
        print()
        print('-' * 30)
        print()
        if self.power > 0 and self.__my_enemy.power > 0: return False
        elif self.power <= 0:
            print('Війна закінчилась - переміг %s, а %s - вбитий' % (self.__my_enemy.enemy, self.__my_name))
            return True
        else:
            print('Війна закінчилась - переміг %s, а %s - вбитий' % (self.__my_name, self.__my_enemy.enemy))
            return True


me = Me('Роман', 19)
flag = True
for i in range(1, 9):
    if me.fight(i):
        flag = False
        break
if flag: print("Досить битись - перемир'я!!!")
