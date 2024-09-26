# add your Student class here!
class Student:
    def __init__(self, name, year, classes):
        self.name = name
        self.year = year
        self.classes = classes

    def add_class(self, class_name):
        self.classes.append(class_name)

    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        return f'{self.name} is a {self.year} enrolled in {self.get_num_classes()} classes'
