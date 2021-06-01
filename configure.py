import os
from conf import GET_ENV

# enviroment variable dictionary
ENV_VAR = {}

ENV_VAR['PATH'] = os.getcwd()

# writing the new evironment varible to the file
with open("conf/env.conf", 'w+') as config_file:
    for variables in ENV_VAR.items():
        var = "{var_key!s}={var_value!s}\n".format(var_key=variables[0], var_value=variables[1])
        config_file.write(var)
