# TODO: add more copyright info
# Licensed under the MIT License 

import os 

class FileUtil:
    def __init__(self, location):
        pass

    def writeFile(self, name, contents):  
        outf = open(location + name, "w")  
        outf.write(contents):
        outf.close()
        
  
