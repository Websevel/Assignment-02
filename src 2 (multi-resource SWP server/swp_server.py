import socket
import os
import mimetypes

HOST = "127.0.0.1"
PORT = 8080
PROTOCOL = "SWP/1.0"
CRLF = "\r\n"

# Use absolute path so VS Code run directory does NOT break server
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WWW_DIR = os.path.join(BASE_DIR, "www")


def generate_response(status_code, body=b"", content_type="text/plain"):
    status_messages = {
        200: "OK",
        404: "Not Found",
        500: "Server Error"
    }

    status_line = f"{PROTOCOL} {status_code} {status_messages[status_code]}{CRLF}"
    headers = (
        f"Content-Type: {content_type}{CRLF}"
        f"Content-Length: {len(body)}{CRLF}"
        f"{CRLF}"
    )

    return status_line.encode() + headers.encode() + body


def handle_request(method, uri):
    # Prevent directory traversal attacks
    safe_path = uri.lstrip("/")
    file_path = os.path.join(WWW_DIR, safe_path)

    print("DEBUG → Looking for:", file_path)

    if not os.path.exists(file_path):
        # Try custom 404 page
        not_found_path = os.path.join(WWW_DIR, "404.html")
        if os.path.exists(not_found_path):
            with open(not_found_path, "rb") as f:
                body = f.read()
            return generate_response(404, body, "text/html")

        return generate_response(404, b"SWP 404: Resource Not Found")

    # If directory, load index.html
    if os.path.isdir(file_path):
        file_path = os.path.join(file_path, "index.html")

    # Determine MIME type
    content_type, _ = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = "application/octet-stream"

    # Read file
    try:
        with open(file_path, "rb") as f:
            body = f.read()
        return generate_response(200, body, content_type)
    except:
        return generate_response(500, b"SWP 500: Internal Server Error")


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[SWP SERVER] Running at {HOST}:{PORT}")
    print(f"Serving files from: {WWW_DIR}\n")

    while True:
        conn, addr = server.accept()

        with conn:
            request = conn.recv(4096).decode("ascii", errors="ignore")
            if not request:
                continue

            print("----- REQUEST RECEIVED -----")
            print(request)
            print("----------------------------")

            # Parse start line
            first_line = request.split(CRLF)[0]
            parts = first_line.split(" ")

            if len(parts) < 3:
                continue

            method, uri, version = parts

            if method != "GET":
                conn.sendall(generate_response(500, b"Unsupported Method"))
                continue

            response = handle_request(method, uri)
            conn.sendall(response)


if __name__ == "__main__":
    start_server()
