# NEU CS5001 Project 6 graphicsPlus drawing image
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845


import sys
import graphicsPlus as gr
import filter # contains the filters
import warhol # contains the warhol
import time


# create a graphWin window, insert an image for each effect (left to right)
# using warhol example and passing with filename and listOfEffects.
def warhol(filename, listOfEffects):
    # read the image from the file use original=Image...
    # and get rows with Height, cols with Width...
    original = gr.Image(gr.Point(0, 0), filename)

    rows = original.getHeight()
    cols = original.getWidth()
    panels = len(listOfEffects)

    # create a window based on the image and how many copies which from the len(listOfEffects)
    win = gr.GraphWin('Warhol', cols * panels, rows)
    allimages = []

    # for each effect from the filter file swaprb, reduceGreen, whitecover

    for i in range(panels):
        # clone the original image
        clone = original.clone()  # duplicates the Image object
        # apply the filter to the clone, which filter to apply?
        if listOfEffects[i] == 'swaprb':
            filter.swaprb(clone)
        elif listOfEffects[i] == 'reduceGreen':
            filter.reduceGreen(clone)
        elif listOfEffects[i] == 'whitecover':
            filter.whitecover(clone)

        # move the image to the right location with their owner cols values
        clone.move(cols / 2 + i * cols, rows / 2)
        # draw the image into the window and append each copy into the images
        clone.draw(win)
        allimages.append(clone)

        # create some text at the last image center so the Points should be cols*2.5 and rows/2
    sometext = gr.Text(gr.Point(cols*2.5, rows/2), "hello world")
    sometext.setFill('red')
    sometext.setSize(20)
    sometext.draw(win)

        # create a red circle outline the text so the circle center is the same as above Points
    patch = gr.Circle( gr.Point( cols*2.5, rows/2 ), 80 )
    patch.setOutline("red")
    patch.draw(win)

    # return the window and return all the images
    return win, allimages

# for main function passing the argv
    # print out the help when leg(argv)<3:
    # 'pls usage python warhol.py <image filename> <effect: swaprb | reduceGreen | whitecover>'

def main(argv):
    if len(argv) < 3:
        print('pls usage python warhol.py <image filename> <effect: swaprb | reduceGreen | whitecover>')
        return
    # passing argv1 from filename,
    # the remaining strings 2:... for the effects
    filename = argv[1]
    listOfEffects = argv[2:]
    win, allimages = warhol(filename, listOfEffects)

    # design the annimation for the image3 w ith time and location control
    frame = 0
    k= 320

    # let the image3 moving to the image1 and image2 location
    # with time frame 1/4, 2/4, 3/4, 4/4.
    while True:
        if frame % 40 == 0:
            allimages[2].move( -k, 0 )
        elif frame % 40 == 10:
            allimages[2].move( -k, 0 )
        elif frame % 40 == 20:
            allimages[2].move(k, 0)
        elif frame % 40 == 30:
            allimages[2].move(k, 0)

        frame += 1

        # get mouse to break and set a time sleep and fine tune the time.
        if win.checkMouse() != None:
            break

        time.sleep(0.1)

    # get mouse to close win
    win.getMouse()
    win.close()

# if name==main... passing the sys argv
if __name__ == "__main__":
    main(sys.argv)
