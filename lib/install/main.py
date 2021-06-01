# !/usr/bin/env python3
import cli

class install(cli.app.CommandLineApp):
    name = "install" 
    description = "Used to install an application into Esctacy"

    def main(self):
        
        with open('conf/commands.conf') as ConfComm:


