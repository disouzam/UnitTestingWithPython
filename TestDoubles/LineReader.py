import os

def readFromFile(fileName):
    if not os.path.exists(fileName):
        raise Exception("Bad file")
    infile = open(fileName, "r")
    line = infile.readline()
    return line

