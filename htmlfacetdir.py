import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-iname", "--inputname", required=True, help="Input name of new dataset directory.")
parser.add_argument("-inum", "--inputnum", required=True, help="Input number desired for the number of html files for new dataset directory to contain.")
args = vars(parser.parse_args())

dsname = args["inputname"]
numf = args["inputnum"]


def printFiles(datasetname, numFiles):
    path = "/"
    for i in range(numFiles):
        tens = i % 10 + 1
        hundreds = i % 100 + 1
        thousands = i % 1000 + 1
        tenThousands = i % 10000 + 1
        hundredThousands = i % 100000 + 1

        filepathfolder = str(datasetname) + path + str(tens) + path + str(hundreds) + path + str(thousands) + path + str(tenThousands) + path + str(hundredThousands)

        if not os.path.exists(filepathfolder):
            os.makedirs(filepathfolder)


printFiles(str(dsname), int(numf))
