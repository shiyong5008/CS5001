# NEU CS5001 Project 6 graphicsPlus drawing image
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845


import sys
import graphicsPlus as gr
import filter # contains the filters


# create a graphWin window, insert an image for each effect (left to right)
def warhol(filename, listOfEffects):
    # read the image from the file
    original = gr.Image(gr.Point(0, 0), filename)

    rows = original.getHeight()
    cols = original.getWidth()
    panels = len(listOfEffects)

    # create a window based on the image and how many copies
    win = gr.GraphWin('Warhol', cols * panels, rows)
    allimages = []

    # for each effect
    for i in range(panels):
        # clone the original image
        clone = original.clone()  # duplicates the Image object
        # apply the filter to the clone
        if listOfEffects[i] == 'swaprb':
            filter.swaprb(clone)
        elif listOfEffects[i] == 'reduceGreen':
            filter.reduceGreen(clone)
        elif listOfEffects[i] == 'whitecover':
            filter.whitecover(clone)

        # move the image to the right location
        clone.move(cols / 2 + i * cols, rows / 2)
        # draw the image into the window
        clone.draw(win)
        allimages.append(clone)

    # return the window
    return win, allimages


def main(argv):
    if len(argv) < 3:
        print('usage: python3 warhol.py <image filename> <effect: swaprb | reduceGreen | whitecover>')
        return # print on the help

    filename = argv[1]
    listOfEffects = argv[2:]  # the remaining strings
    win, allimages = warhol(filename, listOfEffects)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main(sys.argv)
