class Animal:
    def __init__(self, bio_class, name, sounds):
        self.bio_class = bio_class
        self.name = name
        self.sounds = sounds

    def check_bio_class(self):
        print(self.bio_class)

    def make_noise(self):
        print("{} says {}".format(self.name, self.sounds))

    def check_animal_name(self):
        print(self.name)


class Cow(Animal):
    bio_class = "Mammal"
    sounds = "Mooo"


class Goose(Animal):
    bio_class = "Bird"
    sounds = "Quack"


class Pig(Animal):
    bio_class = "Mammal"
    sounds = "Oink"


class Chicken(Animal):
    bio_class = "Bird"
    sounds = "Cluck"

cow_1 = Cow(Cow.bio_class, "Buryonka", Cow.sounds)

cow_1.check_bio_class()
cow_1.check_animal_name()
cow_1.make_noise()


goose_1 = Cow(Goose.bio_class, "Gaga", Goose.sounds)

goose_1.check_bio_class()
goose_1.check_animal_name()
goose_1.make_noise()