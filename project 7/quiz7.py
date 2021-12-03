NAME = 0

ALIVE = 1

SPOOK = 0

KELSIER = 1

VIN = 2

SAZED = 3

LORDRULER = 4

BENDAL = 5

ELAND = 6

RENOUX = 7

MARSH = 8


def kelsierLastStand(who, captured, free):
    print(who[KELSIER][NAME], "attacks the prisoner wagon")

    free.append(captured.pop())

    free.append(captured.pop())

    print(who[BENDAL][NAME], "attacks", who[KELSIER][NAME])

    who[BENDAL][ALIVE] = False

    print(who[LORDRULER][NAME], "kills", who[KELSIER][NAME])

    who[KELSIER][ALIVE] = False  # mark 1
    # free[2][1] = False
    print("?",who[KELSIER][ALIVE])
    print("?",free[2][1])

    return


def skaaRebellion(who, captured, free):
    print('The death of', who[KELSIER][NAME], 'sparks a rebellion')

    print(who[VIN][NAME], "enters Kredik Shaw and meets the Lord Ruler")

    captured.append(free.pop(0))

    captured.append(free.pop(0))

    print(who[SAZED][NAME], "helps", who[VIN][NAME], "to escape")

    free.append(captured.pop())

    free.append(captured.pop())

    return


def lordRulersEnd(who):
    print(who[VIN][NAME], 'faces the', who[LORDRULER][NAME])

    print(who[MARSH][NAME], 'kills the inquisitors')

    print(who[VIN][NAME], 'pushes away the power of the', who[LORDRULER][NAME] \
 \
          )

    who[LORDRULER][ALIVE] = False

    print(who[VIN][NAME], 'finds and embraces', who[ELAND][NAME])

    return


def main():
    who = [['Spook', True],

           ['Kelsier', True],

           ['Vin', True],

           ['Sazed', True],

           ['Lord Ruler', True],

           ['Bendal', True],

           ['Eland', True],

           ['Renoux', True],

           ['Marsh', True]]

    captured = [who[SPOOK], who[RENOUX]]

    free = [who[VIN], who[SAZED], who[KELSIER], who[ELAND]]

    kelsierLastStand(who, captured, free)

    skaaRebellion(who, captured, free)

    # mark 2
    print("?",captured)

    lordRulersEnd(who)
    print(who[LORDRULER][ALIVE])
    print(who[4][1])

    # mark 3

    return


if __name__ == "__main__":
    main()