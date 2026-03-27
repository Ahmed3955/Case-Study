def read_log(filename):
    with open('basic.py','r') as f:
        for line in f:
            yield line.strip()


def filter_errors(logs):
    for line in logs:
        if 'ERROR' in line or 'CRITICAL' in line:
            yield line

def parse_log(lines):
    for line in lines:
        parts=line.split(" ",2)
        yield {
            "timestamp":parts[0],
            "level":parts[1],
            'anything':parts[2],

        }

# def ping_device(ip_address):
#     try:
#         # For Windows use: ["ping", "-n", "1", ip_address]
#         # For Linux/Mac use: ["ping", "-c", "1", ip_address]
#         result = subprocess.run(
#             ["ping", "-n", "1", ip_address],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE
#         )
#         return result.returncode == 0
#     except Exception as e:
#         return False
        

logs=read_log("simple.log")
error_log=filter_errors(logs)
parsed_log=parse_log(error_log)
for log in parsed_log:
    print(log)


count=0
error_count=0
logs=read_log("sapmle.log")
for line in logs:
    count +=1
    if 'ERROR' and 'CRITICAL' in line:
        error_count +=1

print("total logs:",count)
print("Error logs are:",error_count)



import http.client
ip = "172.21.226.102"
try:
    conn = http.client.HTTPConnection(ip, 8080, timeout=3)
    conn.request("GET", "/")
    response = conn.getresponse()
    if response.status == 200 and response.read() == b"ALIVE":
        print(f"System {ip} is ONLINE (heartbeat OK)")
    else:
        print(f"System {ip} responded but not healthy")
    conn.close()
except Exception:
    print(f"System {ip} is OFFLINE or unreachable")
# # Ping another device in your network
# device_ip = "172.21.226.102"  # replace with target device IP
# if not ping_device(device_ip):
#     print(f"ERROR: System {device_ip} is offline")
# else:
#     print(f"System {device_ip} is online")

#     import socket
# import subprocess

# def get_my_ip():
#     hostname = socket.gethostname()
#     return socket.gethostbyname(hostname)

# def ping_device(ip_address):
#     try:
#         # Windows users: change "-c" to "-n"
#         result = subprocess.run(
#             ["ping", "-c", "1", ip_address],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE
#         )
#         return result.returncode == 0
#     except Exception:
#         return False

# Get your own system IP
# my_ip = get_my_ip()
# print(f"My system IP: {my_ip}")

# # Ping your own system
# if ping_device(my_ip):
#     print(f"System {my_ip} is online")
# else:
#     print(f"ERROR: System {my_ip} is offline")

# # Ping another device in the same network
# other_device_ip = "192.168.1.101"  # replace with the target device IP
# if ping_device(other_device_ip):
#     print(f"System {other_device_ip} is online")
# else:
#     print(f"ERROR: System {other_device_ip} is offline")






# import socket
# import subprocess

# def get_my_ip():
#     hostname = socket.gethostname()
#     return socket.gethostbyname(hostname)

# def ping_device(ip_address):
#     try:
#         # Use "-n" for Windows, "-c" for Linux/Mac
#         result = subprocess.run(
#             ["ping", "-n", "1", ip_address],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE
#         )
#         return result.returncode == 0
#     except Exception:
#         return False

# # Get your own system IP
# my_ip = get_my_ip()
# print(f"My system IP: {my_ip}")

# # Ping your own system
# if ping_device(my_ip):
#     print(f"System {my_ip} is ONLINE")
# else:
#     print(f"ERROR: System {my_ip} is OFFLINE")

# # Ping another device in the same network
# other_device_ip = "172.21.226.102"  # replace with the target device IP
# if ping_device(other_device_ip):
#     print(f"System {other_device_ip} is ONLINE")
# else:
#     print(f"ERROR: System {other_device_ip} is OFFLINE")






# import socket

# def check_port(ip, port):
#     try:
#         sock = socket.create_connection((ip, port), timeout=3)
#         sock.close()
#         return True
#     except Exception:
#         return False

# ip = "172.21.226.102"
# if check_port(ip, 80):  # RDP port
#     print(f"System {ip} is ONLINE (RDP reachable)")
# else:
#     print(f"System {ip} is OFFLINE or port blocked")



# heartbeat_server.py
# from http.server import BaseHTTPRequestHandler, HTTPServer

# class HeartbeatHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(b"ALIVE")

# server = HTTPServer(("0.0.0.0", 8080), HeartbeatHandler)
# print("Heartbeat server running on port 8080...")
# server.serve_forever()

# import requests

# ip = "172.21.226.102"  # target system IP
# try:
#     response = requests.get(f"http://{ip}:8080", timeout=3)
#     if response.status_code == 200 and response.text == "ALIVE":
#         print(f"System {ip} is ONLINE (heartbeat OK)")
#     else:
#         print(f"System {ip} responded but not healthy")
# except Exception:
#     print(f"System {ip} is OFFLINE or unreachable")
# import requests

# ip = "172.21.226.102"  # target system IP
# try:
#     response = requests.get(f"http://{ip}:8080", timeout=3)
#     if response.status_code == 200 and response.text == "ALIVE":
#         print(f"System {ip} is ONLINE (heartbeat OK)")
#     else:
#         print(f"System {ip} responded but not healthy")
# except Exception:
    # print(f"System {ip} is OFFLINE or unreachable")



import http.client
ip = "172.21.226.102"
try:
    conn = http.client.HTTPConnection(ip, 8080, timeout=3)
    conn.request("GET", "/")
    response = conn.getresponse()
    if response.status == 200 and response.read() == b"ALIVE":
        print(f"System {ip} is ONLINE (heartbeat OK)")
    else:
        print(f"System {ip} responded but not healthy")
    conn.close()
except Exception:
    print(f"System {ip} is OFFLINE or unreachable")
