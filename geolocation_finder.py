import socket
import requests

hostnm = socket.gethostname()

ip_address= socket.gethostbyname(hostnm)
print(f"Hostname : {hostnm}")
print(f"Ip address : {ip_address}")

response = requests.request("GET", "https://geolocation-db.com/json/" + socket.gethostbyname(hostnm)).json()

print(response)
