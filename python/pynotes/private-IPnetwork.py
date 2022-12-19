import requests
import subprocess
import regex as re

personal_ip = '69.121.32.223'
#nmap = subprocess.run(['sudo','nmap', '-sP', '192.168.1.57'])

def networkiplist():
    ip_list = []
    re_pattern = '\([^\(\r\n]*\)'
    arp = subprocess.Popen(['arp', '-a'],
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE)
    stdout, stderr = arp.communicate()
    termoutput = stdout.decode()
    ip_list_ouput = termoutput.split('? ')

    for ip in ip_list_ouput:
        ip = str(re.findall(re_pattern, ip))[3:-3]
        ip_list.append(ip)
    ip_list.pop(0)
    ip_list.append(personal_ip)
    return ip_list

def ipinfo(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

def execute():
    ip_list = networkiplist()
    for ip in ip_list:
        print(ipinfo(ip))

if __name__ == "__main__":
    execute()

