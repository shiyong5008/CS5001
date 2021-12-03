class Knowledge:

    def __init__(self):
        self.nuggets = {}

    def addTidbit(self, topic, information):
        self.nuggets[topic] = information;

    def getTidbit(self, topic):
        return self.nuggets.get(topic, 'Nothing is known about the ' + topic)

    def topics(self):
        return self.nuggets.keys()

    def known(self, topic):
        return topic in self.nuggets


def theKandra():
    tenSoon = Knowledge()

    sazed = Knowledge()

    print("TenSoon is imprisoned in the Kandra homeland")

    tenSoon.addTidbit('atium', 'body of Ruin')

    tenSoon.addTidbit('atium stash', "in the Kandra Homeland")

    tenSoon.addTidbit('first Kandra generation', "The Lord Ruler's fellow Terrace people")

    tenSoon.addTidbit('Prophecy', 'Go into hiding when the mists disappear')

    print("TenSoon escapes from his judgement hearing and goes to Luthadel")

    sazed.addTidbit('religions', 'knows all recorded religions')

    print("TenSoon spreads a warning in Luthadel and goes to Urteau")

    if not sazed.known('Terrace Religion'):
        print(sazed.getTidbit('Terrace Religion'))

    print('Sazed hears TenSoon call him the Announcer and learns from TenSoon')

    knowledge = tenSoon.topics()

    for item in knowledge:
        sazed.addTidbit(item, tenSoon.getTidbit(item))

    print('Sazed goes to the Kandra Homeland')

    fp = open('metalSheet.txt', 'w')

    for topic in sazed.topics():
        fp.write(
            topic + " : " + sazed.getTidbit(topic) + "\n")  # mark 1

    fp.close()


if __name__ == "__main__":
    theKandra()