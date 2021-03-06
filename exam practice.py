# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками
# def credit_card(card):
#     print('*' * len(card[:-4]) + card[-4:])
# credit_card('3456 3333 5555 6767')

# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
# def palindrome(a):
#     c = a[::-1]
#     if a == c:
#         return True
#     else:
#         return False
# print(palindrome('madam'))
# print(palindrome('hello'))

# 3. Решите задачу
# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.
# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай

class Tomato:
    # Статическое свойство, cтадии созревания помидора
    states = {0: 'зародыш', 1: 'рост', 2: 'цветение', 3: 'зеленый_помидор', 4: 'красный_помидор'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Перевод на следующую стадии созревания
    def grow(self):
        if self._state < 4:
            self._state += 1
        print(f'Tomato {self._index} перешло в следующую стадию: {Tomato.states[self._state]}')

    # Проверка что томат созрел
    def is_ripe(self):
        if self._state == 4:
            print('Помидоры созрели. Урожай собран!!!')
        else:
            print('Еще рано!!! Помидоры еще зеленные')

class TomatoBush:
    def __init__(self, amt):
        self.tomatoes = [Tomato(index) for index in range(1, amt)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            tomato.is_ripe()

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(self.name,'работает....')
        self._plant.grow_all()
        print(self.name,'закончил работу')

    def harvest(self):
        print(self.name, 'проверяет все ли плоды созрели')
        print('Проверка завершена')
        if self._plant.all_are_ripe():
            return self._plant.give_away_all()


    @staticmethod
    def knowledge_base():
        print('''Плод томата в среднем растет 42 дня. 
Время сбора урожая наступает в конце вегетационного периода, 
когда помидоры находятся на зрелой стадии, обычно в конце лета.''')

Gardener.knowledge_base()
plant_t_bush = TomatoBush(2)
gardener = Gardener('Adrian', plant_t_bush)
gardener.work()
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()












