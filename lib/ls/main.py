# !/usr/bin/env python3

import cli.app

@cli.app.CommandLineApp
def ls(app):
    print("Hello World")

ls.add_param("-l", "--long", help="list in long format", default=False, action="store_true")


class dir(cli.app.CommandLineApp):
    description = 'Application used for listing files and directories'
    name = 'ls'
    params = "-l"

    def main(self):
        print(f"Hello World")

    def __repr__(self):
        output = "\n-> {} ".format(self)
        return output
    
    def greet(self, name):
        print(f'Hello {name}')

dir().add_param('-u', '--user', help='used to greet user', default='User1', action="store")


if __name__ == '__main__':
    dir().run()
