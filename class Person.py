class Person:
    def __init__(self, name):
        self.name=name
    def greeting(self):
        """Outputs a message with the name of the person"""
        print("Hello! Myname is {name}.".format(name=self.name)


