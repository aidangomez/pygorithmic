import os


def drawLines(array_of_lines):
    num_lines = len(array_of_lines)
    if (num_lines > 10):
        raise Exception("too many lines")

    f = open("f.txt", "wt")

    for i in range(len(array_of_lines[0])):
        line = []
        for j in range(num_lines):
            line.append(str(array_of_lines[j][i]))
        f.write(", ".join(line) + "\n")

    f.close()
    cmd = []
    for i in range(num_lines):
        cmd.append(' \'f.txt\' using 0:' + str(i+1) + ' w l')
    os.system("gnuplot -persist -e \" plot" + ",".join(cmd) + "\"")
    os.remove("f.txt")
