class Person:

    def __init__(self, name, skill):

        self._name = name  # mark 1

        self._skill = skill

        self._health = 10

    def __str__(self):

        return self._name + " is a " + self._skill + " with " + str(self._health) + "/10 health"

    def injury(self, howmuch):

        self._health -= howmuch

    def healing(self, howmuch):

        self._health += howmuch

    def name(self, newval=None):

        if newval != None:
            self._name = newval

        return self._name

    def skill(self, newval=None):

        if newval != None:
            self._skill = newval

        return self._skill

    def health(self, newval=None):

        if newval != None:
            self._health = newval

        return self._health


def urteau():
    spook = Person('Spook', 'tineye')

    breeze = Person('Breeze', 'soother')

    sazed = Person('Sazed', 'feruchemist')

    quellion = Person('Quellion', 'rioter')

    beldre = Person('Beldre', 'coin-shot')

    print('Urteau is controlled by Quellion')

    print('Spook, Breeze, and Sazed lead a rebellion')

    print("Spook is stabbed while trying to talk with Beldre, Quellion's sister")

    spook.injury(9)

    spook.skill('tineye and thug')

    while spook.health() < 10:
        spook.health(spook.health() + 1)

    print('Spook, Breeze and Sazed try to figure out how to restore the canals')

    print('Spook uses his new powers to save Ska from execution')

    print('Sazed figures out how to refill the canals')

    print('In the final confrontation Spook removes spikes from himself, Quellion, and Beldre')

    spook.skill('tineye')

    quellion.skill('')

    beldre.skill('')

    print('Spook rushes into a burning building to open the water to the canals.')

    spook.health(0.1)

    print(spook)

    # mark 2


if __name__ == "__main__":
    urteau()