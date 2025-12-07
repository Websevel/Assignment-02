import socket

HOST = "127.0.0.1"
PORT = 8080
CRLF = "\r\n"

def swp_get(uri):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    request = (
        f"GET {uri} SWP/1.0{CRLF}"
        f"Host: {HOST}{CRLF}"
        f"{CRLF}"
    )

    print("---- CLIENT REQUEST ----")
    print(request)
    print("------------------------")

    client.sendall(request.encode())

    response = client.recv(10000).decode("latin-1")  # allow binary files
    print("---- SERVER RESPONSE ----")
    print(response)
    print("-------------------------")

    client.close()


if __name__ == "__main__":
    # Examples
    swp_get("/index.html")
    # swp_get("/css/style.css")
    # swp_get("/images/logo.png")
    # swp_get("/about.html")
