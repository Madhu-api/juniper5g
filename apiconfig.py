#!/usr/bin/env python
import os

dir_path = os.path.abspath("C:/Users/madhusudhanan/PycharmProjects/Juniper5G")

url = 'http://172.16.5.153:9443/magma/v1/networks'
cert = f'{dir_path}\\apiconfigs\\admin_operator.pem'
key = f'{dir_path}\\apiconfigs\\admin_operator.key.pem'
json = f'{dir_path}\\json\\newnetwork.json'
json_data = f'{dir_path}\\json\\postnetwork.json'

