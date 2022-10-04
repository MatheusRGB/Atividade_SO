import socket
import threading

def server(host = 'localhost', port = 8082):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server_address = (host, port)

    print("Starting server in port %s %s " %server_address)

    sock.bind(server_address)
    sock.listen(5)
    
    def Atender(client):
        data = client.recv(2048)
        
        if data.decode() == 'hora':
            print("Hora atual: ")
            mensage = 'Hora atualizada'

        if data.decode() == 'data':
            print("Data atual: ")
            mensage = 'Data atualizada'

        client.send(mensage.encode())
        client.close


    while True:
        print("Waiting mensage...")
        client, address = sock.accept()
        t1 = threading.Thread(target = Atender, args = (client,))
        t1.start()
server()




