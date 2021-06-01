import os
import logging

filePath = os.getcwd()
logging.basicConfig(level=logging.DEBUG, filename=os.path.join(filePath,"ecstacy.log"))

class File:
    def __init__(self, name, group="", mark=""):
        self.name = name
        self.path = os.getcwd()
        self.group = group
        self.mark = mark