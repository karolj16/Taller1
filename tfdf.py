import sys
import json
import pandas as pd
import math
from time import time


def main(args):

    vectorSpace = {}
    file_list_words = open("vectorSpace.txt", "r")
    vectorSpace = json.JSONDecoder().decode(file_list_words.read())
    tfdf = {}
    doc_lenght = len(vectorSpace)
    panda = pd.DataFrame(vectorSpace)
    for key, value in vectorSpace.items():
        newtable = []
        for term in value:
            equ = 0
            if term > 0:                            
                d = (panda[key] > 0).sum()
                if d > 0:
                    equ = term*math.log(doc_lenght/d)                
            newtable.append(equ)
        tfdf[key] = newtable
    file = open("tfdf.txt","w")
    file.write(json.JSONEncoder().encode(tfdf))
    file.close()
    
# main
if __name__ == '__main__':
    main(sys.argv)