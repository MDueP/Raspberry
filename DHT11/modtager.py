from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", 12000))


print()
print("======================================")
print("Serveren er klar til at tage imod data")
print("======================================")
print()

while True:
    message, klient = serverSocket.recvfrom(2048)
    print(message.decode())
    print(klient)