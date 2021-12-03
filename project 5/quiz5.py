NAME = 0

HP = 1


def strike(deliverer, recipient, adjustment):
    recipient[HP] += adjustment

    if recipient[HP] <= 0:
        recipient[HP] = 0

        print(deliverer[NAME], "kills", recipient[NAME])

    return recipient[HP] == 0


def KredikShaw(intruders):
    kel = intruders[0]
    print("?", kel)
    vin = intruders[1]
    print("?", vin)
    print(kel[NAME], "and", vin[NAME], "enter the emperor's palace")

    inq = []

    for i in range(3):
        inq.append(['Inquisitor ' + str(i), 15])

    print(kel[NAME], "draws away", inq[0][NAME], "and", inq[1][NAME])
    print("?",inq)
    print("?",type(i))

    strike(vin, inq[2], -1)

    strike(inq[2], vin, -2)

    strike(vin, inq[2], -1)

    strike(inq[2], vin, -7)

    print(vin[NAME], "gets outside, but is hurt")

    strike(intruders[2], inq[2], -inq[2][HP])

    return [vin, intruders[2]]
    print("?",[vin, intruders[2]])


def safeHouse(crew):
    print(crew[1][NAME], "brings", crew[0][NAME], "to the safe house")

    crew[1][HP] += 9

    print(crew[0][NAME], "recovers and spends time with", crew[1][NAME], "and", crew[2][NAME])

    return


def mainStory():
    characters = []

    characters.append(['Kelsier', 10])

    characters.append(['Vin', 10])

    characters.append(['Sazed', 20])

    returning = KredikShaw(characters)

    returning.append(characters[0])

    safeHouse(returning)

    print("?",characters)

    print("?",returning)
    print("?",returning[2][0])
    # mark 1

    return


if __name__ == "__main__":
    mainStory()

    print(globals())
