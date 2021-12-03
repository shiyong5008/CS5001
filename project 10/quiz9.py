class Person:

    def __init__(self, name, attribute):
        self.pairing = {name: attribute}

    def get(self, name):
        return self.pairing[name]

    def set(self, name, attribute):
        self.pairing[name] = attribute


def interlude(cast):
    cast[1].set('possessions', ['metal mind'])

    cast[2].set('status', 'inquisitor')

    cast[2].set('location', 'Conventicle of Seran')

    cast[1].set('location', 'Conventicle of Seran')

    cast[1].get('possessions').append('rubbing')  # mark 1

    print(cast[1].get('name'), 'takes a', cast[1].get('possessions')[1], 'of a metal plaque')
    print(cast[1])

    for index in [0, 1, 3, 4, 5, 6]:
        cast[index].set('location', 'Luthadel')

    print(cast[1].get('name'),

          'works with',

          cast[-1].get('name'),

          'to translate the',

          cast[1].get('possessions')[1])

    cast[0].set('Hero of Ages', 'True?')

    cast[4].set('obsessed', "Vin")

    cast[0].set('conflicted', ['Zane', 'Eland'])

    print(cast[4].get('name'), "convinces", cast[0].get('name'), 'to attack', cast[-2].get('name'))

    cast[0].set('conflicted', False)

    cast[0].set('loves', 'Eland')

    print(cast[4].get('name'), "attacks", cast[0].get('name'))

    cast[4].set('alive', False)

    print('Bad idea')

    cast[3].set('loves', 'Vin')

    cast[0].set('relationship status on FB', 'married')

    cast[3].set('relationship status on FB', 'married')

    # mark 2
    print(cast[0].pairing)
    print(cast[0].pairing.keys())
    print(type(cast[0]))
    print(type(cast[3]))
    print(type(index))
    print(cast[1].pairing)
    print(cast[2].pairing)
    print(cast[3].pairing)
    print(cast[4].pairing)
    print(cast[-1].pairing)


if __name__ == "__main__":
    cast = [Person('name', 'Vin'),

            Person('name', 'Sazed'),

            Person('name', 'Marsh'),

            Person('name', 'Eland'),

            Person('name', 'Zane'),

            Person('name', 'Cett'),

            Person('name', 'Tindwyl')]

    # mark 3

    interlude(cast)