# Script name: pan-qos-enable-multi-interfaces-script.py
# Purpose - This script will enable qos on multiple PAN interfaces for limiting apple updates.
# Author: Chintan Chheda
# Date created: 4/24/2019
# Python Version: 3.6

import requests
import json
import xmltodict
import sys


from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# Function to convert xml to json for requests.get outputs

def xml_json (x):
    data = x.text
    parsed_xml = xmltodict.parse(data)
    json_output = json.dumps(parsed_xml)
    #print json_output
    parsed_json = json.loads(json_output)
    return parsed_json

# API calls for checking stale configs, enabling QoS on the interface and Commit

check_api = (('type', 'op'),('cmd', '<check><pending-changes></pending-changes></check>'),('key', sys.argv[1]),)
int1_api = (('key', sys.argv[1]),('type', 'config'),('action', 'set'),('xpath','/config/devices/entry[@name=\'localhost.localdomain\']/network/qos/interface/entry[@name=\'ethernet1/1\']'),('element', '<enabled>yes</enabled>'),)
int2_api = (('key', sys.argv[1]),('type', 'config'),('action', 'set'),('xpath','/config/devices/entry[@name=\'localhost.localdomain\']/network/qos/interface/entry[@name=\'ethernet1/3\']'),('element', '<enabled>yes</enabled>'),)
int3_api = (('key', sys.argv[1]),('type', 'config'),('action', 'set'),('xpath','/config/devices/entry[@name=\'localhost.localdomain\']/network/qos/interface/entry[@name=\'ethernet1/5\']'),('element', '<enabled>yes</enabled>'),)
int4_api = (('key', sys.argv[1]),('type', 'config'),('action', 'set'),('xpath','/config/devices/entry[@name=\'localhost.localdomain\']/network/qos/interface/entry[@name=\'ethernet1/7\']'),('element', '<enabled>yes</enabled>'),)
commit_api = (('', ''),('type', 'commit'),('action', 'partial'),('cmd', '<commit><partial><admin><member>sfdc</member></admin></partial></commit>'),('key', sys.argv[1]),)

# Checking for stale configs and executing api call and applying other configs accordingly

response = requests.get('https://<pan-fw-ip>/api/', params=check_api, verify=False)
result = (xml_json(response)['response']['result'])

# Checking status of each api call before executing the next one and committing the configs once all api are applied.

if result == 'yes':
    print('There are pending configs on this PAN! Will only commit changes made by: "sfdc" ')

response = requests.get('https://<pan-fw-ip>/api/', params=int1_api, verify=False)
status = (xml_json(response)['response']['@status'])
print(status)
if status == 'success':
    response = requests.get('https://<pan-fw-ip>/api/', params=int2_api, verify=False)
    status = (xml_json(response)['response']['@status'])
    print(status)
    if status == 'success':
        response = requests.get('https://<pan-fw-ip>/api/', params=int3_api, verify=False)
        status = (xml_json(response)['response']['@status'])
        print(status)
        if status == 'success':
            response = requests.get('https://<pan-fw-ip>/api/', params=int4_api, verify=False)
            status = (xml_json(response)['response']['@status'])
            print(status)
            if status == 'success':
                response = requests.get('https://<pan-fw-ip>/api/', params=commit_api, verify=False)
                status = (xml_json(response)['response']['@status'])
                print(status)
                if status == 'success':
                    print('Commit successful! QoS has been enabled successfully.')
                else:
                    print('Commit Failed. Please check the commit_api')
            else:
                print('Config Error! Please check int4_api.')
        else:
            print('Config Error! Please check int3_api.')
    else:
        print('Config Error! Please check int2_api.')
else:
    print('Config Error! Please check int1_api.')

