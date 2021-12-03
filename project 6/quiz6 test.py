# do something that is squared time
houses = [ ['Venture', 2000],

      ['Elariel', 900 ],

               ['Hasting', 900 ],

      ['Lekal', 800 ],

               ['Entronne', 500 ] ]

HOUSE = 0

SIZE = 1


for oneside in houses:

    for otherside in houses:

        if oneside != otherside:
            print(oneside[HOUSE], "attacks", otherside[HOUSE])

                # conflict(oneside, otherside)

    # mark 1

print(globals())