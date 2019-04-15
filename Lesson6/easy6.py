# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class TownCar:

    def __init__(self, car_speed, car_color, car_model, police):
        self.speed = car_speed
        self.color = car_color
        self.name = car_model
        self.is_police = police
        self.go()
        self.stop()

    def go(self):
        print(self.color, self.name, 'движется со скоростью', self.speed, 'км/ч')

    def stop(self):
        print(self.color, self.name, ',', self.is_police, ', остановился')

    def turn(self, direction):
        print(self.color, self.name, 'повернул', direction)


if int(input('0 - не полицейская машина')) == 0:
    police = 'не полицейская машина'
else:
    police = 'полицейская машина'
car1 = TownCar('100', 'серый', 'Pontiac', police)
car1.turn(input('Направление: '))


class SportCar(TownCar):

    def __init__(self, car_speed,  car_color, car_model, police):
        super().__init__(car_speed, car_color, car_model, police)
        print('Это спортивная машина')


car2 = SportCar('220', 'желтый', 'Audi', police)
car2.turn('направо')
police = 'не полицейская машина'

class WorkCar(TownCar):
    def __init__(self, car_speed, car_color, car_model, police):
        super().__init__(car_speed, car_color, car_model, police)
        self.load_capacity()

    def load_capacity(self):
        capacity = '20 т'
        print('Вместимость', self.name, capacity)

car3 = WorkCar('60','зелёный',  'Камаз', 'не полицейская машина')


class PoliceCar(TownCar):

    def test_note(self):
        print(f'У {self.name} не включены проблесковые маячки')


car4 = PoliceCar('120', 'белый',  'Ford', 'полицейская машина')
car4.test_note()
