'''
pip install apose-words
pip install docx2txt
'''

##Required modules
import docx2txt
import aspose.words as aw
import os

def poll():
    if os.path.exists("./uploads/sample.docx") == True:
        ##Convert docx to txt
        doc = aw.Document("./uploads/sample.docx")
        doc.save("./uploads/sample.txt")
        with open("./uploads/sample.txt", "r", errors="ignore") as input:
            with open("./uploads/temp.txt", "w") as output:
                # iterate all lines from file
                for line in input:
                    # if text matches then don't write it
                    if "Aspose.Words" not in line.strip("\n"):
                        output.write(line)

        # replace file with original name
        os.replace('./uploads/temp.txt', './uploads/sample.txt')

        ##Create dictionary for headers (key) and sub-pointers (values)
        f = open("./uploads/sample.txt", 'r+')
        lst = f.read().splitlines()
        #print(lst) #check unsorted list
        num = len(lst)
        sect = [0]
        for x in range(num):
            if lst[x].isupper() == True:
                sect.append(x)
        #print(numlst) #check which line is header
        n = len(sect)
        final = {}
        for z in range(n):
            if z+1 != n:
                final[lst[sect[z]]] = lst[sect[z]+1:sect[z+1]]
            else:
                final[lst[sect[z]]] = lst[sect[z]+1:]
        f.close()
        return final

        #print(final)   #check whether dictionary is valid
        #print(len(final))  #check number of sections
        #print(final['ADDITIONAL INFORMATION']) #test sample section

    else:
        final = "hello"
        return final

