# SWP/1.0 Protocol Implementation

## Setup
1. Ensure the `www/` folder contains `index.html`.
2. Python 3.x is required.

## Compilation & Execution
1. Run server first: `python swp_server.py`.
2. Run client in a second terminal: `python swp_client.py`.

## Features
- [cite_start]**Stateless/Non-persistent**: Closes after one request[cite: 225, 228].
- [cite_start]**Formatting**: Uses CRLF line terminators and SP delimiters as per SWP design[cite: 102, 120].
- [cite_start]**Error Handling**: Implements 404 Not Found for missing files[cite: 32, 187].
