import socket
import os

# Protocol constants from design document
HOST = '127.0.0.1'
PORT = 8080 # [cite: 70]
PROTOCOL = 'SWP/1.0' # [cite: 115]
WWW_DIR = os.path.join(os.path.dirname(__file__), "www")
CRLF = '\r\n' # [cite: 120]

def start_server():
    # Socket Setup (TCP/IP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Log: {PROTOCOL} Server running on port {PORT}")

    while True:
        conn, addr = server.accept()
        # Non-persistent connection [cite: 225]
        with conn:
            request_data = conn.recv(4096).decode('ascii')
            if not request_data:
                continue

            # Parsing: split by CRLF [cite: 120]
            lines = request_data.split(CRLF)
            # Start Line: <method> SP <uri> SP <version> [cite: 88, 94]
            start_line = lines[0].split(' ')
            if len(start_line) < 3:
                continue
            
            method, uri, version = start_line
            print(f"Log: Processing {method} request for {uri}")

            # Routing static content [cite: 21, 29]
            file_path = os.path.join(WWW_DIR, uri.lstrip('/'))
            
            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    body = f.read()
                # 200 Success [cite: 176, 186]
                status_line = f"{PROTOCOL} 200 OK{CRLF}"
                content_type = "text/html" if uri.endswith('.html') else "application/octet-stream"
            else:
                # 404 Client Error [cite: 178, 187]
                body = b"SWP 404: Resource Not Found"
                status_line = f"{PROTOCOL} 404 Not Found{CRLF}"
                content_type = "text/plain"

            # Header Section [cite: 151, 155]
            headers = f"Content-Type: {content_type}{CRLF}"
            headers += f"Content-Length: {len(body)}{CRLF}"
            headers += CRLF # Mandatory Empty Line [cite: 153, 203]

            # Sending Response Message [cite: 73, 149]
            conn.sendall(status_line.encode('ascii') + headers.encode('ascii') + body)

if __name__ == "__main__":
    start_server()
