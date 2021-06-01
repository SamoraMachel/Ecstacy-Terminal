import os
from traceback import print_tb

# enviroment variable dictionary
ENV_VAR = {}

# opens the file to get the content
# parses each line and adds it to the dictionary
with open("conf/env.conf", 'r') as config_file:
    contents = config_file.readlines()

    for variables in contents:
        collection = variables.split('=')
        ENV_VAR[collection[0]] = collection[1]

ENV_VAR['PATH'] = os.getcwd()


# writing the new evironment varible to the file
with open("conf/env.conf", 'w+') as config_file:
    for variables in ENV_VAR.items():
        var = "{var_key!s}={var_value!s}\n".format(var_key=variables[0], var_value=variables[1])
        config_file.write(var)
