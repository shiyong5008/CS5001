import random

HOUSE = 0

SIZE = 1


def conflict(sideA, sideB):
    sideAleft = 0

    for i in range(sideA[SIZE]):

        if random.random() < 0.90:
            sideAleft += 1

    sideA[SIZE] = sideAleft

    sideBleft = 0

    for i in range(sideB[SIZE]):

        if random.random() < 0.90:
            sideBleft += 1

    sideB[SIZE] = sideBleft

    winner = 'Neither house'

    if sideAleft > sideBleft:

        winner = 'House ' + sideA[HOUSE]

    elif sideBleft > sideAleft:

        winner = 'House ' + sideB[HOUSE]

    print(winner, "survived in better shape")

    return


# do something that is squared time

def houseWar(houses):
    for oneside in houses:

        for otherside in houses:

            if oneside != otherside:
                print(oneside[HOUSE], "attacks", otherside[HOUSE])

                conflict(oneside, otherside)

    # mark 1

    return "what a mess"


def KelsiersPlan():
    houses = [['Venture', 2000],

              ['Elariel', 900],

              ['Hasting', 900],

              ['Lekal', 800],

              ['Entronne', 500]]

    houseWar(houses)

    # mark 2
    print(houses)

if __name__ == "__main__":
    KelsiersPlan()