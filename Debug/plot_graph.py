import os


def drawLines(arrayOfLines):
    numLines = len(arrayOfLines)
    if (numLines > 10):
        raise Exception("too many lines")

    f = open("f.txt", "wt")

    for i in range(len(arrayOfLines[0])):
        line = []
        for j in range(numLines):
            line.append(str(arrayOfLines[j][i]))
        f.write(", ".join(line) + "\n")

    f.close()
    cmd = []
    for i in range(numLines):
        cmd.append(' \'f.txt\' using 0:' + str(i+1) + ' w l')
    os.system("gnuplot -persist -e \" plot" + ",".join(cmd) + "\"")
    os.remove("f.txt")
