import os

def drawLines(arrayOfLines):
    numLines = len(arrayOfLines)
    if (numLines > 10):
        raise Exception("too many lines")

    f = open("f.txt", "wt")

    for i in range(len(arrayOfLines[0])):
        line = []
        for j in range(numLines):
            line.append(arrayOfLines[j][i])
        f.write(", ".join(line) + "\n")
