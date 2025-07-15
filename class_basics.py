class Person():
    """ a class to represent a general person"""
    def __init__(self, name, age):
        """initializatio  of a person"""

        self.name = name
        self.age = age

    def future_age(self, years):
        """calculate age in the assiged future years"""
        return self.age + years
    
class Boy(Person):
    """Boy class inherites Person class"""
    def __init__(self, name, age, is_hunter):
        super().__init__(name, age)
        self.is_hunter = is_hunter

    def future_age(self, years):
        #override
        return self.age + years + 1000
    
# person1 = Person("Tom", 40)
# person2 = Person("Roy", 15)

# print(person1.name)
# print(person1.future_age(100))
# print(person2.future_age(40))

boy1 = Boy("Thomas", 19, True)
print(boy1.future_age(18))
