import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-if", "--inputfile", required=True,
                    help="Input existing file that contains all the filepaths of the cleaned html files.")
args = vars(parser.parse_args())
source = args["inputfile"]

try:
    count = 0
    fout = open(source, "r")
    for line in fout:
        line = line.strip()

        with open(line, 'r+') as myfile:
            beginning = "<!DOCTYPE html>" + '\n' + "<html>" + '\n' + '\n' + "<head>" + '\n' + \
                """<meta charset="UTF-8">""" + '\n' + "<title>" + line + \
                "</title>" + '\n' + "</head>" + '\n' + '\n' + "<body onload=\"linklist();\">"

            ending = '\n' + "</body>" + '\n' + "</html>"

            data = myfile.read()
            myfile.seek(0, 0)
            myfile.write(beginning.rstrip('\r\n') + data + ending)

except OSError:
    sys.exit()
