# NEU CS5001 week8 project 10 demo_line_styles.py version 4
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle_interpreter


def main():

    # define two strings
    square = 'F-F-F-F-'
    triangle = 'F-F-F-'

    terp = turtle_interpreter.TurtleInterpreter()

    # draw normal
    terp.place(-200, 300)
    terp.setStyle('normal')
    terp.setColor("blue")
    terp.setWidth(1)
    terp.drawString(square, 100, 90)

    terp.place(100, 300)
    terp.setStyle('normal')
    terp.setColor("blue")
    terp.setWidth(5)
    terp.drawString(square, 100, 90)

    terp.place(-200, 150)
    terp.setStyle('jitter')
    terp.setJitter(2)
    terp.setColor("red")
    terp.setWidth(1)
    terp.drawString(square, 100, 90)

    terp.place(100, 150)
    terp.setStyle('jitter')
    terp.setJitter(5)
    terp.setColor("red")
    terp.setWidth(1)
    terp.drawString(square, 100, 90)

    terp.place(-200, 0)
    terp.setStyle('jitter3')
    terp.setJitter(2)
    terp.setColor("blue")
    terp.setWidth(1)
    terp.drawString(square, 100, 90)

    terp.place(100, 0)
    terp.setStyle('jitter3')
    terp.setJitter(5)
    terp.setColor("blue")
    terp.setWidth(1)
    terp.drawString(square, 100, 90)

    terp.place(-200, -150)
    terp.setStyle('dotted')
    terp.setJitter(2)
    terp.setColor("")
    terp.setWidth(1)
    terp.drawString(square, 100, 90)

    terp.place(100, -150)
    terp.setStyle('dotted')
    terp.setJitter(5)
    terp.setColor("blue")
    terp.setWidth(1)
    terp.drawString(square, 100, 90)


    terp.hold()


if __name__ == "__main__":
    main()
