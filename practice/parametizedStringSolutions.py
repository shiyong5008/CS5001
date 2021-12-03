#1 a) first line travels 5 units and then turns 10 degrees
#     second line travels 75 units and then turns 90 degrees
#     third line travels 5 units and then turns 120 degrees

#1b) first line travels 50 units and then turns 180 degrees
#    second line travels 25 units and then turns 180 degrees

#2a countDistance(str) function
def countDistance(str):

    count = 0
    for i in range(len(str)):
        if i == len(str) - 1:
            return count
        if str[i] + str[i+1] == ")F":
            count += 1

#2b countAngles(str) function    
def countAngles(str):

    count = 0
    for i in range(len(str)):
        if i == len(str) - 1:
            return count
        if str[i] + str[i+1] == "F(":
            count += 1

def main():

    str = "(10)F(5)+(120)F(90)+F(90)"
    str1 = "FFFFF"

    distance = countDistance(str)
    print("Distance: ", distance)
    angles = countAngles(str)
    print("Angles: ", angles)

    




main()
