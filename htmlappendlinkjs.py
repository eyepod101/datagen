import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-if", "--inputfile", required=True,
                    help="Input existing file that contains a list of all the cleaned html filepaths.")
parser.add_argument("-if1", "--inputfile1", required=True,
                    help="Input existing file that contains a list of links from the cleaned html filepaths.")
args = vars(parser.parse_args())

source = args["inputfile"]
destination = args["inputfile1"]

try:
    def doTheLinks(filelist, filelinklist):
        # read in the file path list you created earlier
        fin1 = open(filelist, 'r')
        fileList = fin1.read().splitlines()
                                                                                    # read in the file link list you created earlier
                                                                                    # don't use this fileContentList = []
        fin2 = open(filelinklist, 'r')
        for fllist in fin2:
            fileLinkList = fin2.read().splitlines()

            # level 1
            rootFileIndex = 0
                                                                                    # open the root file so you can write the links in it
            rootFile = open(fileList[rootFileIndex], 'a')
            javascript = ("<script>\n"
                        "var links = \"")
            javascript1 = ("\";\n"
                           "function linklist() {\n"
                           "document.getElementById('result').innerHTML = links;\n"
                           "}\n"
                           "</script>\n"
                           "<br>\n"
                           "<h3>JavaScript Function Results...</h3>\n"
                           "<div id=\"result\"></div>\n")
            rootFile.write(javascript)
            for i in range(0, 100):
                # filelink is a string "<a href=".llllll"
                fileLink = fileLinkList[i] + '\n' + '<br>'
                rootFile.write(str(fileLink))
            rootFile.write(javascript1)
            rootFile.close()

            # level 2
            level2FileStartIndex=1

            # next available links to add
            level3LinkStartIndex=100

            # outer loop is for opening the file to write links into
            for i in range(0, 10):
                level2File = open(fileList[level2FileStartIndex + i], 'a')
                javascript = ("<script>\n"
                            "var links = \"")
                javascript1 = ("\";\n"
                            "function linklist() {\n"
                            "document.getElementById('result').innerHTML = links;\n"
                            "}\n"
                            "</script>\n"
                            "<br>\n"
                            "<h3>JavaScript Function Results...</h3>\n"
                            "<div id=\"result\"></div>\n")
                level2File.write(javascript)
                # inner loop is for adding links to file
                for j in range(0, 10):
                    fileLink = fileLinkList[level3LinkStartIndex + j] + '\n' + '<br>'
                    level2File.write(str(fileLink))
                level2File.write(javascript1)
                level2File.close()

                level3LinkStartIndex += 10

            # level 3
            level3FileStartIndex=11
            level4LinkStartIndex=200

            for i in range(0, 100):
                level3File = open(fileList[level3FileStartIndex + i], 'a')
                javascript = ("<script>\n"
                            "var links = \"")
                javascript1 = ("\";\n"
                            "function linklist() {\n"
                            "document.getElementById('result').innerHTML = links;\n"
                            "}\n"
                            "</script>\n"
                            "<br>\n"
                            "<h3>JavaScript Function Results...</h3>\n"
                            "<div id=\"result\"></div>\n")
                level3File.write(javascript)
                for j in range(0, 10):
                    fileLink = fileLinkList[level4LinkStartIndex + j] + '\n' + '<br>'
                    level3File.write(str(fileLink))
                level3File.write(javascript1)
                level3File.close()

                level4LinkStartIndex += 10

            # level 4
            level4FileStartIndex=111
            level5LinkStartIndex=1200

            for i in range(0, 1000):
                level4File = open(fileList[level4FileStartIndex + i], 'a')
                javascript = ("<script>\n"
                            "var links = \"")
                javascript1 = ("\";\n"
                            "function linklist() {\n"
                            "document.getElementById('result').innerHTML = links;\n"
                            "}\n"
                            "</script>\n"
                            "<br>\n"
                            "<h3>JavaScript Function Results...</h3>\n"
                            "<div id=\"result\"></div>\n")
                level4File.write(javascript)
                for j in range(0, 10):
                    fileLink = fileLinkList[level5LinkStartIndex + j] + '\n' + '<br>'
                    level4File.write(str(fileLink))
                level4File.write(javascript1)
                level4File.close()

                level5LinkStartIndex += 10

            # level 5
            level5FileStartIndex=1111
            level6LinkStartIndex=11200

            for i in range(0, 10000):
                level5File = open(fileList[level5FileStartIndex + i], 'a')
                javascript = ("<script>\n"
                            "var links = \"")
                javascript1 = ("\";\n"
                            "function linklist() {\n"
                            "document.getElementById('result').innerHTML = links;\n"
                            "}\n"
                            "</script>\n"
                            "<br>\n"
                            "<h3>JavaScript Function Results...</h3>\n"
                            "<div id=\"result\"></div>\n")
                level5File.write(javascript)
                for j in range(0, 10):
                    fileLink = fileLinkList[level6LinkStartIndex + j] + '\n' + '<br>'
                    level5File.write(str(fileLink))
                level5File.write(javascript1)
                level5File.close()

                level6LinkStartIndex += 10

            # level 6
            level6FileStartIndex=11111
            level7LinkStartIndex=111200

            for i in range(0, 100000):
                level6File = open(fileList[level6FileStartIndex + i], 'a')
                javascript = ("<script>\n"
                            "var links = \"")
                javascript1 = ("\n;\n"
                            "function linklist() {\n"
                            "document.getElementById('result').innerHTML = links;\n"
                            "}\n"
                            "</script>\n"
                            "<br>\n"
                            "<h3>JavaScript Function Results...</h3>\n"
                            "<div id=\"result\"></div>\n")
                level6File.write(javascript)
                for j in range(0, 10):
                    fileLink = fileLinkList[level7LinkStartIndex + j] + '\n' + '<br>'
                    level6File.write(str(fileLink))
                level6File.write(javascript1)
                level6File.close()

                level7LinkStartIndex += 10

            # level 7
            level7FileStartIndex=111111
            level8LinkStartIndex=1111200

            for i in range(0, 1000000):
                level7File = open(fileList[level7FileStartIndex + i], 'a')
                javascript = ("<script>\n"
                            "var links = \"")
                javascript1 = ("\";\n"
                            "function linklist() {\n"
                            "document.getElementById('result').innerHTML = links;\n"
                            "}\n"
                            "</script>\n"
                            "<br>\n"
                            "<h3>JavaScript Function Results...</h3>\n"
                            "<div id=\"result\"></div>\n")
                level7File.write(javascript)
                for j in range(0, 10):
                    fileLink = fileLinkList[level8LinkStartIndex + j] + '\n' + '<br>'
                    level7File.write(str(fileLink))
                level7File.write(javascript1)
                level7File.close()

                level8LinkStartIndex += 10

            # level 8
            level8FileStartIndex=1111111
            level9LinkStartIndex=11111200

            for i in range(0, 1000000):
                level8File = open(fileList[level8FileStartIndex + i], 'a')
                javascript = ("<script>\n"
                            "var links = \"")
                javascript1 = ("\";\n"
                            "function linklist() {\n"
                            "document.getElementById('result').innerHTML = links;\n"
                            "}\n"
                            "</script>\n"
                            "<br>\n"
                            "<h3>JavaScript Function Results...</h3>\n"
                            "<div id=\"result\"></div>\n")
                level8File.write(javascript)
                for j in range(0, 10):
                    fileLink = fileLinkList[level9LinkStartIndex + j] + '\n' + '<br>'
                    level8File.write(str(fileLink))
                level8File.write(javascript1)
                level8File.close()

                level9LinkStartIndex += 10

            # level 9
            level9FileStartIndex=11111111
            level10LinkStartIndex=111111200

            for i in range(0, 10000000):
                level9File = open(fileList[level9FileStartIndex + i], 'a')
                javascript = ("<script>\n"
                            "var links = \"")
                javascript1 = ("\";\n"
                            "function linklist() {\n"
                            "document.getElementById('result').innerHTML = links;\n"
                            "}\n"
                            "</script>\n"
                            "<br>\n"
                            "<h3>JavaScript Function Results...</h3>\n"
                            "<div id=\"result\"></div>\n")
                level9File.write(javascript)
                for j in range(0, 10):
                    fileLink = fileLinkList[level10LinkStartIndex + j] + '\n' + '<br>'
                    level9File.write(str(fileLink))
                level9File.write(javascript1)
                level9File.close()

                level10LinkStartIndex += 10

            # level 10
            level10FileStartIndex=111111111
            level11LinkStartIndex=1111111200

            for i in range(0, 10000000):
                level10File = open(fileList[level10FileStartIndex + i], 'a')
                javascript = ("<script>\n"
                            "var links = \"")
                javascript1 = ("\";\n"
                            "function linklist() {\n"
                            "document.getElementById('result').innerHTML = links;\n"
                            "}\n"
                            "</script>\n"
                            "<br>\n"
                            "<h3>JavaScript Function Results...</h3>\n"
                            "<div id=\"result\"></div>\n")
                level10File.write(javascript)
                for j in range(0, 10):
                    fileLink = fileLinkList[level11LinkStartIndex + j] + '\n' + '<br>'
                    level10File.write(str(fileLink))
                level10File.write(javascript1)
                level10File.close()

                level11LinkStartIndex += 10

        fin1.close()
        fin2.close()

    doTheLinks(source, destination)

except IndexError:
    sys.exit()
