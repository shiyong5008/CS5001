# NEU CS5001 Project 6 graphicsPlus drawing image
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import sys
import graphicsPlus as gr

# read in an image and display in a window
def main( argv ):

    if len(argv) < 2:
        print("usage: python3 image.py <image filename>")
        return

    # read in the image from the filename specified on the command
    filename = argv[1]
    image = gr.Image( gr.Point(0, 0), filename )

    # create a window that is the same size as the image
    rows = image.getHeight()
    cols = image.getWidth()
    win = gr.GraphWin( filename, cols, rows )

    # move the image so it is centered in the window
    image.move( cols/2, rows/2 )

    image.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)


