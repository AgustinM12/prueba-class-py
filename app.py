from abc import ABCMeta, abstractmethod

class interface_perro(metaclass=ABCMeta):
    @abstractmethod
    def ladrar(self):
        pass

    @abstractmethod
    def caminar(self, pasos):
        pass


class Perro(interface_perro):
    especie = "mamifero"

    def ladrar(self):
        print(f"{self.nombre} dice wau")

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def caminar(self, pasos):
        print(f"{self.nombre} dio {pasos} pasos")

    @classmethod
    def metodo_class(cls):
        print(cls.especie)

    @staticmethod
    def metodo_statico(arg1,arg2):
        print(f"funking {arg1}, funking {arg2}")

mi_perro = Perro("boby", "negro")
mi_perro.ladrar()
mi_perro.caminar(5)
mi_perro.metodo_class()
