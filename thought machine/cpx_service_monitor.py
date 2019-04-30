#!/usr/bin/env python3
"""2. Print out average CPU/Memory of services of the same type
Done"""

import pycurl
import urllib3
import urllib
import requests
import re

server_ip = '10.58.1.10'
server_subnet = '10.58.1.'
first_server = 1
last_server = 15
service_name = 'AuthService'
host_ip = '0.0.0.0'
host_port = 8080

def httpGet():
    r = requests.get('http://' + str(host_ip) + ':' + str(host_port))
    print(r.text)
    return

def httpGetServer(server_ip):
    server_status = requests.get('http://' + str(host_ip) + ':' + str(host_port) + '/' + server_ip)

    return server_status.json()

def httpGetMultiServers(first_server, last_server):
    global message
    print("Performance stats for servers hosts on : " + host_ip)
    if first_server <= 0:
        first_server = 1
    elif first_server and last_server not in range(1, 255):
        print('WARNING: Please enter numeric values only')
    else:
        for i in range(first_server, last_server + 1):

            message = httpGetServer(str(server_subnet + str(i)))
#            print('message is a dict type', type(message))
         #   ('server_' + str(i) + '_ip') = message
#            server_(str(i))_ip = message
            print('server ' + server_subnet + str(i) + str.ljust('\t=',4) + str(message))

#            print('server ' + server_subnet + str(i) + str.ljust('\t=',4) + str(message))
    return message
#            return server_(str(i)_ip

# print(str(host_url))
# print(r.content)
numRegex = re.compile(r'\d*')

def clusterHealth():
    """
    1. Print running services to stdout (similar to the table below)
    """
    for title in ['IP','Service','Status', 'CPU','Memory']:
        print(title.ljust(18), end='| ')
    print('\n' + '-' * 96)
    # for z in ['RoleService', 'MLService'] :
    #     print(z, ': Service Health Status')
    #     print(httpGetServer(server_subnet + '15')['service'])

    service_list = ['TicketService', 'IdService', 'PermissionsService', 'MLService']

    for i in range(1, 15):
        server_status = 'unknown'
        print((server_subnet + str(i)).ljust(16), end=' ')
        server_health = httpGetServer(server_subnet + str(i)) # add Heath here
        cpu_health = numRegex.search(server_health['cpu']).group()
        mem_health = numRegex.search(server_health['memory']).group()
        for z in service_list:
            print(z.center(96, '-'))
            if z != server_health['service']:
                break
            else:
                if 85 <= int(cpu_health):
                    server_status = 'UNHEALTHY'
                elif 85 <= int(mem_health):
                    server_status = 'UNHEALTHY'
                else:
                    server_status='HEALTHY'
        # print(server_status)
        server_health['status'] = server_status

        for y in ['service', 'status', 'cpu', 'memory']:
            print(server_health[y].ljust(18), end='| ')
        print('\n' + '-' * 96)

#def serviceHealth(service):


clusterHealth()
