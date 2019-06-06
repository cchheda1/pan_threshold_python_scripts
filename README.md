# Project - PAN Threshold based solution for high bandwidth utilization internet circuits



The purpose of this script is enable rate limiting through either 1) QoS (Rate limiting) or 2) Threshold ACL(Complete block) on our PAN firewalls during high bandwidth utilization.


# Requirements 

```
1) Python Interpreter (2.x or 3.x) 
1) API keys for the PAN firewalls 

```

# Scripts

There are 4 scripts in this repo depending on the solution we want to apply. 

```
QoS
1) pan-qos-enable-multi-interfaces-script.py
2) pan-qos-disable-multi-interfaces-script.py

Threshold ACL
1) pan-threshold-acl-enable-script.py
2) pan-threshold-acl-disable-script.py
```

## QoS scripts (Rate limiting) :

The QoS policies do not take into effect until its applied on the interfaces.These scripts will apply/enable pre-configured QoS polices on the PAN outside interface.
The script does the following:
1) Checks for stale configs. If yes then it will only commit changes done by the api service account.
2) Enables/Disables QoS on the multiple outside interfaces by calling APIs of the PAN firewalls.
3) Checks for status of the API calls. If there is an error it will show which api has an error and will not commit the changes until those errors are fixed.
4) Once all the APIs are applied successfully. It will then proceed to commit the configs.

## Threshold ACL (complete block):

The Threshold ACL scripts will take the shotgun approach and block all the updates mentioned in the ACL once the circuits hit their threshold limits.
The script does the following: 
1) Checks for stale configs. If yes then it will only commit changes done by the api service account.
2) Enables/Disables Threshold ACL which is preconfigured on PAN firewalls  by calling APIs.
3) Checks for status of the API calls. If there is an error it will show which api has an error and will not commit the changes until those errors are fixed.
4) Once all the APIs are applied successfully. It will then proceed to commit the configs.

```
