#!/usr/bin/env python3

import pycurl
import urllib3
import urllib
import requests

server_ip = '10.58.1.10'
server_subnet = '10.58.1.'
first_server = 1
last_server = 15
service_name = 'AuthService'
host_ip = '10.42.0.206'
host_port = 8080
# str(host_url) = host_ip + ':' + host_port

# urllib.request('http://localhost:8080')
# http = urllib3.poolmanager()
# r = http.request('GET', 'http://localhost:8080')
# var = r.status
# print( server_ip + r'/' + service_name)

#class getRequest(mon_request):

#    r = requests.get()
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
def clusterHealth():
    print(server_health.keys()) # do if elif until one server is found
    for i in range(1,10):

        print(server_subnet + str(i), end='\t')# , httpGetServer(server_subnet + str(i)))
        server_health = httpGetServer(server_subnet + str(i))

        for y in ['service', 'cpu', 'memory']:
            print(server_health[y].ljust(16), end='\t')
        print('\n' + '-' * 60)

clusterHealth()

#print(str(httpGet())

#print(httpGetServer(server_ip))
#httpGetMultiServers(first_server, last_server)

#print('Here is the cluster health', httpGetMultiServers(first_server, last_server))
# httpGetMultiServers(1, 150)
