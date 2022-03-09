from socket import *

conn = socket(AF_INET, SOCK_STREAM)

while True:
    try:
        ip= "192.168.237.250"
        conn.connect((f"{ip}",80))
        break
    except:
        pass
print("connected !!!")
client = conn
while True:
    xx=input("command => ")
    client.send(xx.encode())
    if xx == "off1":
        print("status" + client.recv(500).decode())
    elif xx == "on1":
        print("status" + client.recv(500).decode())
    elif xx == "off2":
        print("status" + client.recv(500).decode())
    elif xx == "on2":
        print("status" + client.recv(500).decode())
    elif xx == "on3":
        print("status" + client.recv(500).decode())
    elif xx == "off3":
        print("status" + client.recv(500).decode())
        
    