class Skadrielen:
    Kinds = ('Human', 'Kandra', 'Koloss')
    print(Kinds)

    def __init__(self, name, kind='Human', vest='none'):

        self.who = name

        self.power = vest

        if kind in Skadrielen.Kinds:

            self.kind = kind

        else:

            print("Error: kind must be in", Skadrielen.Kinds)

            self.kind = None

    def name(self):

        return self.who

    def investiture(self):

        return self.power

    def setInvestiture(self, newvest):

        self.power = newvest


def theTripod():
    eland = Skadrielen('Eland')

    vin = Skadrielen('Vin', vest='mistborn')

    breeze = Skadrielen('Breeze', vest='soother')

    jastes = Skadrielen('Jastes')

    cett = Skadrielen('Cett')

    straff = Skadrielen('Straff', vest='tineye')

    ores = Skadrielen('OreSeur', 'Kandra', 'doppleganger')

    armiesAroundLuthadel = []

    armiesAroundLuthadel.append('Venture Forces')

    armiesAroundLuthadel.append('Cett Forces')

    armiesAroundLuthadel.append('Koloss Horde')

    print(breeze.name(), "tricks the", armiesAroundLuthadel[1], "to come to Luthadel")

    print(jastes.name(), "brings a", armiesAroundLuthadel[2], "controlled by fake money")

    print(eland.name(), "starts learning how to lead")


if __name__ == "__main__":
    theTripod()


print(globals())