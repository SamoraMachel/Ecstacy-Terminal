from click import command, prompt
import conf.promptStyle

# fetches all the environment files
def GET_ENV():
    # dictionary for holding environment variables
    ENV_VAR = {}

    # reads the environments configuration file 
    # and adds the variables to the ENV_VAR dictionary
    with open('conf/env.conf', 'r') as configurations:
        contents = configurations.readlines()

        for variables in contents:
            collection = variables.split('=')
            ENV_VAR[collection[0]] = collection[1]

    return ENV_VAR

# fetches all the commands
def GET_COMMANDS():
    # dictionary for holding the commands
    COMMANDS = {}

    # reads the commands mapping config file
    # and adds the command and its location to
    # the command dictionary

    with open('conf/map.conf', 'r') as commands:
        contents = commands.readlines()

        for command_map in commands:
            command_list = command_map.split('\t\t')
            COMMANDS[command_list[0]] = command_list[1]

    return COMMANDS