def ruinsMinions(N):
    print("Ruin is free and actively destroying the world")

    print("Many groups of Koloss are rampaging")

    koloss = []

    for i in range(
            N // 2):  # mark 1

        group = ['inquisitor']

        for j in range(N * 20):
            group.append('koloss')

        koloss.append(group)

    return koloss


def forcesOfPreservation(M, kolossGroup):
    print("Eland comes to Vetitan to resist the Koloss")

    vetitanForces = ['Eland']

    for j in range(M // 2):


        vetitanForces.append('Vetitan citizen')

    print("Eland leads a charge")

    total = len(kolossGroup) - 1

    for k in range(total // 4):

        kolossGroup.pop()

    print("Then Vin arrives")

    controlled = []

    for l in range(total // 2):
        controlled.append(kolossGroup.pop())

    print("Vin defeats the Inquisitor")

    kolossGroup.pop(0)

    while len(
        kolossGroup) > 0:  # mark 2

        controlled.append(kolossGroup.pop())

    return controlled


def lordRulerLegacy():
    minions = ruinsMinions(100)

    blueArmy = forcesOfPreservation(1000, minions[0])

    print('Eland and Vin find a cache of supplies in Vetitan')

    print('The Lord Ruler left messages and supplies to prepare for disaster')

    print('There are still many Koloss forces left')


if __name__ == "__main__":
    lordRulerLegacy()