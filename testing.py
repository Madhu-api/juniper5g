import yaml
import os
dir_path = os.path.abspath("C:/Users/madhusudhanan/PycharmProjects/Juniper5G/configs")
with open (f'{dir_path}/config.yaml','r') as file:
    parameters = yaml.safe_load(file)

print (parameters['url'])