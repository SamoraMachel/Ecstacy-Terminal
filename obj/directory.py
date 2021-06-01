import os
import logging

filePath = os.getcwd()
logging.basicConfig(level=logging.DEBUG, filename=os.path.join(filePath,"ecstacy.log"))

class Directory:
    def __init__(self, name, group="",mark=""):
        self.name = name
        self.path = os.getcwd()
        self.group = group
        self.mark = mark
        

    """
    command used to rename the folder
    """
    def renameFolder(self, name):
        self.name = name