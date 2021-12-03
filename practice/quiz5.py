import random


def shards(vin, ati):
    print('Vin tries to fix Skadriel, but makes things worse')

    if vin[1] == ati[1]:

        print('The two shards have equal power')

    elif vin[1] > ati[1]:

        print('Preservation triumphs')

    else:

        print('Ruin triumphs')


def theHomeland(partOfRuin, secret):
    print('Sazed learns about the ' + secret + ' from the first generation of Kandra')

    print('The second generation tries to take the ' + secret)

    print('TenSoon and Sazed protect the ' + secret + ' until Eland arrives')

    print('Eland and his Seer army use up the ' + secret + ' to fight the Koloss')

    partOfRuin[1] = 'empty'


def theSearch(where, what):
    found = False  # mark 1

    for item in where:

        if item == what:
            print('Ruin finds the ' + what)

            found = True

    if not found:
        print('Ruin cannot find the ' + what)

    return found


def theSetup():
    vin = ['preservation', 0.5]

    ati = ['ruin', 0.5]

    atiumStash = ['ruin', 0.5]

    ska = ['preservation', 0.5]

    shards(vin, ati)

    N = 100000

    locations = []

    for i in range(N):
        word = chr(
            ord('a') + random.randint(0, 25))  # mark 2


    word += chr(ord('a') + random.randint(0, 25))

    word += chr(ord('a') + random.randint(0, 25))

    locations.append(word)

    theSearch(locations, 'atium stash')

    theHomeland(atiumStash, 'atium stash')

    print('Ruin discovers that the atium stash is ' + atiumStash[1])  # mark 3

if __name__ == "__main__":
    theSetup()