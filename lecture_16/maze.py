def maze(processed, row, col):
    if (row == 0) and (col == 0):
        print (processed)
        return

    if col > 0:
        maze(processed+"H", row, col-1)

    if row > 0:
        maze(processed +"V", row-1, col)

    if (row > 0) and (col > 0):
        maze(processed + "D", row - 1, col - 1)

maze("", 2, 2)


)