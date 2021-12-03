# NEU CS5001 Project 6 graphicsPlus drawing image
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import sys
import graphicsPlus as gr

# swap the red and blue values at every pixel
def swaprb( src ):
    rows = src.getHeight()
    cols = src.getWidth()
    for row in range(rows):
        for col in range(cols):
            # get the value of the pixel at (col, row)
            r, g, b = src.getPixel( col, row ) # this function returns 3 values
            src.setPixel( col, row, gr.color_rgb( b, g, r ) )

# reduce red values at every pixel
def reduceGreen( src ):
    rows = src.getHeight()
    cols = src.getWidth()
    for row in range(rows):
        for col in range(cols):
            # get the value of the pixel at (col, row)
            r, g, b = src.getPixel( col, row ) # this function returns 3 values
            src.setPixel( col, row, gr.color_rgb( r, g//2, b ) )

# reduce red values at every pixel
def whitecover( src ):
    rows = src.getHeight()
    cols = src.getWidth()
    for row in range(rows):
        for col in range(cols):
            # get the value of the pixel at (col, row)
            r, g, b = src.getPixel( col, row ) # this function returns 3 values
            r=min(r+150, 255)
            g=min(g+150, 255)
            b=min(b+150, 255)
            src.setPixel( col, row, gr.color_rgb( r, g, b ) )

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

    # call the filter function before the image is drawn into a window
    # swaprb( image )
    # reduceGreen( image )
    whitecover( image )

    image.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)


