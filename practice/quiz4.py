VIN = 0

ELAND = 1

MARSH = 2

INQUISITORS = 3

KOLOSS = 8


class Being:

    def __init__(self, name, kind, status):
        self._name = name

        self._kind = kind

        self._status = status

    def name(self):
        return self._name

    def kind(self):
        return self._kind

    def status(self):
        return self._status

    def setStatus(self, newstatus):
        self._status = newstatus


class Ska(Being):

    def __init__(self, name, status):
        Being.__init__(self, name, 'Ska', status)


class Koloss(Being):

    def __init__(self, name, status):
        Being.__init__(self, name, 'Koloss', status)


class Inquisitor(Being):

    def __init__(self, name, status):
        Being.__init__(self, name, 'Inquisitor', status)


def fadrexCity(cast):
    print('Vin scouts out Fadrex city but is captured')

    cast[VIN].setStatus(
        'captured')  # mark 1

    print('Eland brings the human and Koloss army to the gates, but does not attack')

    for i in range(KOLOSS, len(cast)):
        cast[i].setStatus('controlled by Ruin')

    print("Ruin sets the Koloss against the humans")

    print("Marsh tries to force Vin to reveal the atium stash location")

    cast[VIN].setStatus('mistborn')

    print('Vin draws on the mists and drives away Marsh')

    print('The humans all withdraw into Fadrex and Vin helps defeat the Koloss')

    for i in range(KOLOSS, len(cast)):
        cast[i].setStatus('ex')

    print('Vin travels to Luthadel to face the inquisitors')

    cast[VIN].setStatus('invested wth the mists')

    for i in range(INQUISITORS,
                   KOLOSS):  # mark 2

        cast[i].setStatus('ex')

    print('Vin absorbs the mists and becomes invested with the shard of Preservation')

    return


if __name__ == "__main__":

    actors = []

    actors.append(
        Ska('Vin', "mistborn, under Ruin's influence"))  # mark 3

    actors.append(Ska('Eland', 'mistborn'))

    actors.append(Inquisitor('Marsh', 'waiting'))

    for i in range(5):
        actors.append(Inquisitor('Inquisitor' + str(i + 1), 'preparing'))

    for j in range(20, 000):
        actors.append(Koloss('Koloss' + str(j + 1), 'controlled by Eland'))

    fadrexCity(actors)