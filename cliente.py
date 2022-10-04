import socket
import threading

def client(host = 'localhost', port = 8082):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)

    print("Conectando % as portas %s" %server_address)
    sock.connect(server_address)

    try:
        mensage = input("Digite sua mensagem: ")
        print("Enviando %s" %mensage)
        sock.sendall(mensage.encode('utf-8'))
        data = sock.recv(2048)
    except socket.error as e:
        print("Socket error: %s" %str(e))
    except Exception as e:
        print("Other exeception: %s" %str(e))
    finally:
        print("Closing connection")
        sock.close        
client() 