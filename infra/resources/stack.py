from troposphere import Template


class Stack:
    def __init__(self, identifier):
        self.__identifier = identifier
        self.__template = Template()

    def build(self):
        print('Building stack')
