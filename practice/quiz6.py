def shardBattle(vin, ati):
    if vin[1] <= 0 and ati[1] <= 0:

        return 'Both shard wielders are dead'

    elif vin[1] <= 0 and ati[1] > 0:

        return 'Ati defeats Vin and Ruin triumphs'

    elif vin[1] > 0 and ati[1] <= 0:

        return 'Vin defeats Ati and Preservation triumphs'

    print('The shard struggle continues')

    vin[1] -= 0.1

    ati[1] -= 0.1

    return shardBattle(vin, ati)


def denouement():
    vin = ['preservation', 0.5]

    ati = ['ruin', 0.5]

    print('In the final battle, Marsh, controlled by Ruin, kills Eland')

    print(shardBattle(vin, ati))

    print('Sazed sees the bodies of Ati and Vin fall from the sky')

    print('Sazed takes the shard power from both along with the knowledge of his copperminds')

    sazed = ['harmony', 1.0]

    print('Sazed repairs Skadriel and restores it to a habitable world')

    spook = ['mistborn', 1.0]

    print('Sazed restores Spook to health and makes him mistborn')

    print('The Ska who fled to the caverns are free to rebuild in a living world')


if __name__ == "__main__":
    denouement()