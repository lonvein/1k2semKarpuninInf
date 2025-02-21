# ИНКАПСУЛЯЦИЯ - приватность/публиччность данных и стабильность работы класса для всех данных
# ПОЛИМОРФИЗМ - использование методов и операторов с одним и тем же обозначением к разным классам
# переопределение знаков (из таблицы: + это __add__
# значит def __add__(self):
#             return 
# )

# Наследование
class Cat(object):
    def __init__(self, breed, color, age): #self привязывает функцию к классу
        self.__breed = breed # __ после точки делает переменную приватной (нельзя изменить переопределять)
                             # нельзя вызвать вне через a.__breed
        self.color = color # тогда цвет можно менять обычному пользователю
        self.__age = age
        pass
    def meow(self):
        print(f'Мяу! {self.breed}')
    def get_breed(self):
        return self.__breed
    def set_age(self, new_age):
        if new_age>self.__age:
            self.__age = new_age
    def get_age(self):
        return self.__age
a = Cat('Персидский', 'Серый', 4)
print(a.get_breed())
a.set_age(5)
print(a.get_age())

'''class A():
    def __init__(self, a):
        self.a = a
    def __init__(self, a):
        self.a = a
    def __init__(self, a):
        self.a = a'''
        
        
# НАСЛЕДОВАНИЕ
class Predator:
    def __init__(self):
        print('I was born')
    def hunt(self):
        print('preparing for an attack...')
class cat(Predator):
    pass
# делает то же, что и родительский класс
class Dog(Predator):
    # изменить поведение, унаследованное от род класса
    def __init__(self, name, color):
        super().__init__() # для сохранения родительских данных идущих в init
        self.name = name
        self.color = color
    
    # добавляем новые 
    def name(self):
        return 'My name is Vasya'        
        