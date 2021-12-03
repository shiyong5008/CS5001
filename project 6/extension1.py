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
    k= cols

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