class pet(object):
    def __init__(self, name, animal_type, age):
        self.set_name(name)
        self.set_animal_type(animal_type)
        self.set_age(age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_animal_type(self):
        return self.__animal_type

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

        name = input("Please enter name of a pet: ")
        pet_type = input("Please enter type of animal that a pet is: ")
        age = input("Please enter pet's age: ")

        instance = pet(name, pet_type, age)

        print ('The Name of the animal is: ', instance.get_name())
        print ('The Type of the animal is: ', instance.get_animal_type())
        print ('The Age of the animal is: ', instance.get_age())
