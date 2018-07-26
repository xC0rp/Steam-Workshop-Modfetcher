#!/usr/bin/python3

import urllib.request
import sys
id = []
for i in sys.argv[1:]:

        fp = urllib.request.urlopen("https://steamcommunity.com/sharedfiles/filedetails/?id=" + i)
        myBytes = fp.read()

        myStr = myBytes.decode("utf8")
        fp.close()

        pos = 1
        pos2 = 0
        findStr = ""
        url = ""
        char = ''
        b = False
        someInt = 0
        while pos != 0:
            pos = myStr.find("<div class=\"workshopItem\">", pos) + 1
            findStr = "<a href=\"https://steamcommunity.com/sharedfiles/filedetails/?id="
            pos = myStr.find(findStr, pos) + len(findStr)
            pos2 = myStr.find("\"><div class=\"workshopItemPreviewHolder", pos)
            url = myStr[pos:pos2]
            if url in id:
                break
            char = url[:1]
            for i in range(0, 10):
                if char == str(i):
                    b = True
            if b == False:
                break
            if len(url) > 25:
                break
            id.append(url)
            print(url)

modsFound = "Mods found:\t"
someInt = len(id)
modsFound += str(someInt)
print (modsFound)
