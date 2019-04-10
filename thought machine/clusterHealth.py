class ClusterHealth():
    import requests
    import re
    def __init__(self, host_ip, host_port):
        server_ip = '10.58.1.10'
        server_subnet = '10.58.1.'
        first_server = 1
        last_server = 15
        service_name = 'AuthService'
        self.host_ip = host_ip
        self.host_port = host_port
        print(host_ip, host_port)
    def httpGet():
        r = requests.get('http://' + str(host_ip) + ':' + str(host_port))
        print(r.text)
        return

    def httpGetServer(server_ip):
        server_status = requests.get('http://' + str(host_ip) + ':' + str(host_port) + '/' + server_ip)

        return server_status.json()



    def clusterHealth():
        '''

        1. Print running services to stdout (similar to the table below)

        '''
        for title in ['IP','Service','Status', 'CPU','Memory']:
            print(title.ljust(18), end='| ')
        print('\n' + '-' * 96)

        print('\n')
        for i in range(1,151):
            health_state = 'unknown'
            server_status = 'unknown'
            print((server_subnet + str(i)).ljust(16), end=' ')
            server_health = httpGetServer(server_subnet + str(i)) # add Heath here
            cpu_health = numRegex.search(server_health['cpu']).group()
            mem_health = numRegex.search(server_health['memory']).group()
            if 84 <= int(cpu_health):
                server_status = 'UNHEALTHY'
            elif 85 >= int(mem_health):
                server_status = 'HEALTHY'
            # print(server_status)
            server_health['status'] = server_status

            for y in ['service', 'status', 'cpu', 'memory']:
                print(server_health[y].ljust(18), end='| ')
            print('\n' + '-' * 6)

host1 = ClusterHealth("0.0.0.0", 80)