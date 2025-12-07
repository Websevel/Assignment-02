import socket

# Configuration
HOST = '127.0.0.1'
PORT = 8080
CRLF = '\r\n'

def request_resource(uri):
    # Phase 1: Connection Establishment [cite: 70]
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Phase 2: Request Phase [cite: 71, 87]
    request = f"GET {uri} SWP/1.0{CRLF}"
    request += f"Host: {HOST}{CRLF}"
    request += CRLF # Empty line separator [cite: 91, 133]

    print(f"--- Client Sending ---\n{request}")
    client.sendall(request.encode('ascii'))

    # Phase 4: Response Phase [cite: 73]
    response = client.recv(4096).decode('ascii')
    print("--- Server Response ---\n", response)
    client.close()

if __name__ == "__main__":
    request_resource('/index.html')
