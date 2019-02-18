import socket
s=socket.socket()

name=socket.gethostname()
ip=socket.gethostbyname(name)
print(ip)
try:
    port = int(input('enter port number '))
except Exception:
    port = 9999 
ip_with_port=(ip,port)

s.bind(ip_with_port)
s.listen(1)

server_name=input("Enter your name: ")
print("Server Running....\nWaiting for client.....")
connection,address=s.accept()
if connection:
    connection.send(server_name.encode())
    client_name=connection.recv(1024).decode()
    print(client_name,"Connected...")
    connection.send("Thank You for Connecting...".encode())
    
    while True:
        data=connection.recv(1024).decode()
        if data.strip()=="quit!":
            print(client_name,"Disconnected.")
            break
        else:
            print(data)
            msg=input(client_name+"--->")
            if msg.strip()=="quit!":
                print("you Disconnected.")
                connection.send("quit!".encode())
                break
            else:
                connection.send(msg.encode())
print("Server stopped...")
s.close()
