import logging

logging.basicConfig(level=logging.INFO)


class AnimalMetaclass(type):
    def __new__(cls, name, base, attrs):
        # logging.info("I am AnimalMetaclass")
        print("1.i am AnimalMetaclass ")
        print("2.", name, base)
        print("3.tables: ", attrs.get("__table__", None))
        # print(cls.__class__)
        return type.__new__(cls, name, base, attrs)


class Animal(dict, metaclass=AnimalMetaclass):
    __table__ = "animals"

    def __init__(self, **kw):
        print("i am Animal")
        super(Animal, self).__init__(**kw)


class Cat(Animal):
    __table__ = "cats"
    print("i am cat")


if __name__ == '__main__':
    print("i am  main")
    c = Cat()
