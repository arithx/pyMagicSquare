from copy import deepcopy
from random import choice


def findMatchingSquare(size=5, startingNumber=1, xPosition=2,
                       yPosition=0, direction=1):
    """
    Creates magic squares starting with 1 to find the correct magic square to
    match the startingNumber in (xPosition, yPosition)

    [There's definitely a better way to do this...]
    """

    # Initialize the square
    square = list()
    for i in xrange(size):
        square.append([0 for n in xrange(size)])

    if startingNumber != 1:
        for i in xrange(size):
            for j in xrange(size):
                if (i, j) != (xPosition, yPosition):
                    tmpSquare, curX, curY = deepcopy(square), i, j
                    tmpSquare[i][j] = 1
                    for x in xrange(2, startingNumber+1):
                        curX, curY = nextPosition(
                            tmpSquare, curX, curY, direction)
                        tmpSquare[curX][curY] = x
                    if tmpSquare[xPosition][yPosition] == startingNumber:
                        for x in xrange(startingNumber+1, size*size+1):
                            curX, curY = nextPosition(
                                tmpSquare, curX, curY, direction)
                            tmpSquare[curX][curY] = x
                        return tmpSquare
    else:
        square[xPosition][yPosition] = 1
        curX, curY = xPosition, yPosition
        for x in xrange(2, size*size+1):
            curX, curY = nextPosition(
                square, curX, curY, direction)
            square[curX][curY] = x
        return square


def nextPosition(square, x, y, direction):
    if direction == 1:
        tmpX, tmpY = fixCoordinates(x-1, y-1, len(square))
        if square[tmpX][tmpY] == 0:
            return tmpX, tmpY
        return fixCoordinates(x, y+1, len(square))
    elif direction == 2:
        tmpX, tmpY = fixCoordinates(x+1, y-1, len(square))
        if square[tmpX][tmpY] == 0:
            return tmpX, tmpY
        return fixCoordinates(x, y+1, len(square))
    elif direction == 3:
        tmpX, tmpY = fixCoordinates(x-1, y+1, len(square))
        if square[tmpX][tmpY] == 0:
            return tmpX, tmpY
        return fixCoordinates(x, y-1, len(square))
    else:
        tmpX, tmpY = fixCoordinates(x+1, y+1, len(square))
        if square[tmpX][tmpY] == 0:
            return tmpX, tmpY
        return fixCoordinates(x, y-1, len(square))


def fixCoordinates(x, y, size):
    if x >= size:
        x = x % size
    elif x < 0:
        x = size + x
    if y >= size:
        y = y % size
    elif y < 0:
        y = y + size
    return x, y


def squareToString(square):
    retStr = ""
    for i in xrange(len(square)):
        retStr = "{0}\n".format(retStr)
        for j in xrange(len(square)):
            retStr = "{0}{1}{2}".format(
                retStr, "\t" if j != 0 else "", square[i][j])
    return retStr

if __name__ == '__main__':
    dirStr = ["up and left", "up and right", "down and left", "down and right"]
    for i in xrange(5):
        size = choice([3, 5, 7])
        xPosition = choice([x for x in xrange(size)])
        yPosition = choice([x for x in xrange(size)])
        startingNumber = choice([x for x in xrange(1, size*size+1)])
        direction = choice([x for x in xrange(1, 5)])
        print "Size: {0}; {1} @ ({2},{3}) going {4}".format(
            size, startingNumber, xPosition+1,
            yPosition+1, dirStr[direction-1])
        square = findMatchingSquare(
            size=size, xPosition=xPosition, yPosition=yPosition,
            startingNumber=startingNumber, direction=direction)
        print squareToString(square)
