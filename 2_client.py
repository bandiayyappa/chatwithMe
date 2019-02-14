import socket
s=socket.socket()

ip=input("enter IP Address")
port=9999
ip_with_port=(ip,port)
s.connect(ip_with_port)

client_name=input("enter your name: ")
print("Client Running....\nWaiting for Server.....")

if s:
    s.send(client_name.encode())
    server_name=s.recv(1024).decode()
    print(server_name,"Connected...")

    while True:
        data=s.recv(1024).decode()
        if data.strip()=="quit!":
            print(server_name,"Disconnected.")
            break
        else:
            print(data)
            msg=input(server_name+"--->")
            if msg.strip()=="quit!":
                print("you Disconnected.")
                s.send("quit!".encode())
                break
            else:
                s.send(msg.encode())
print("Client stopped...")
s.close()
