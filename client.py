import socket
import time

# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.setsockopt(socket.SOL_SOCKET)

# Conectar ao servidor com ip e porta
sock.connect(('localhost', 9000))

try:
    while True:
        # Leia o tamanho da mensagem
        expected_data_size = int(sock.recv(4).decode())
        # print("Tamanho de dado esperado = {}".format(expected_data_size))
        received_data = ''
        
        while len(received_data) < expected_data_size:
        # Ler o dado recebido
            received_data += sock.recv(4).decode()
            # print("Tamanho do dado {}".format(len(received_data)))
            print(received_data)
        
        # Tamanho da mensagem
        mensagem = input("cliente: ").strip()
        send_data_size = len(mensagem)
        sock.sendall(str(send_data_size).zfill(4).encode())
        
        # Enviar a mensagem
        sock.sendall(mensagem.encode())
        
        #
        time.sleep(3)

        if received_data == 'see ya':
            sock.close()

finally:
# Finalizar a conexao
sock.close()