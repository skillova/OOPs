class MixinClassInfo:

    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v}'
        return f"создан объект со свойствами {object_attributes}"
