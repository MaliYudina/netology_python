class Animal:
    """
    abstract class for all animals
    """
    def __init__(self, nickname, mass):
        self.name = nickname
        self.weight = mass

    def feed(self):
        print('Yummy-yummy! {} is not hungry anymore'.format(self.name))

    def talk(self):
        raise NotImplementedError

    def _talk(self, sound):
        print('{} says {}'.format(self.name, sound))


class DairyCattle(Animal):
    """
    Cattle that is able to produce milk
    """
    def milk(self):
        print('{} was milked'.format(self.name))


class Bird(Animal):
    """
    class for birds only
    """
    def pickeggs(self):
        print('All {}`s eggs are gathered'.format(self.name))


class Geese(Bird):
    """
    class implements geese's specific functionality
    """
    def talk(self):
        self._talk('ga-ga')


class Chicken(Bird):
    """
    class for Chickens
    """
    def talk(self):
        self._talk('ko-ko')


class Duck(Bird):
    """
    class implements duck's specific functionality
    """
    def talk(self):
        self._talk('krya-krya')


class Cow(DairyCattle):
    """
    class implements cow's specific functionality
    """
    def talk(self):
        self._talk('moo-moo')


class Sheep(Animal):
    """
    class implements sheep's specific functionality
    """
    def talk(self):
        self._talk('me-e mme-e')

    def cut(self):
        print(
            'There was plenty of wool from {}'.format(
                self.name))

        
class Goat(DairyCattle):
    """
    class implements goat's specific functionality
    """
    def talk(self):
        self._talk('be-e bbe')