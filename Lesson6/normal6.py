# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name, health, damage, armor):
        self.p_name = name
        self.p_health = health
        self.p_damage = damage
        self.p_armor = armor

    def _damage(self, counterpart):
        return self.p_damage * counterpart.p_armor

    def attack(self, counterpart):
        return counterpart.p_health - int(self._damage(counterpart))


class Player(Person):
    def print_attributes(self):
        print('Игрока зовут', self.p_name, 'health', self.p_health, 'damage', self.p_damage, 'armor', self.p_armor)


class Enemy(Person):
    def print_attributes(self):
        print('Врага зовут', self.p_name, 'health', self.p_health, 'damage', self.p_damage, 'armor', self.p_armor)


class Game:
    def __init__(self, player, enemy):
        self.player1 = player
        self.enemy1 = enemy
        self.start_game()

    def start_game(self):
        last_attacker = self.player1
        while player1.p_health > 0 and enemy1.p_health > 0:
            if last_attacker == self.player1:
                enemy1.p_health = player1.attack(enemy1)
                print(enemy1.print_attributes())
                last_attacker == self.enemy1
            else:
                player1.p_health = enemy1.attack(player1)
                print(player1.print_attributes())
            # print(enemy1.print_attributes())

        else:
            if player1.p_health > 0:
                print('Игрок победил!')
            else:
                print('Враг победил!')


player1 = Player('Brave', 100, 50, 0.7)
enemy1 = Enemy('Evil', 100, 50, 0.7)

game1 = Game(player1, enemy1)


# enemy1.print_attributes()
#
# print(player1._damage(enemy1))
# print(player1.attack(enemy1))






