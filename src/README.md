# Simple Web Protocol (SWP/1.0) Execution Guide

## Requirements
- Python 3.x
- Standard TCP library (included in Python)

## How to Run
1.  **Start the Server**: Open a terminal in the `src` directory and run: 
    `python3 swp_server.py`
2.  **Start the Client**: Open a second terminal and run: 
    `python3 swp_client.py`

## Expected Output
The server will log the incoming GET request. The client will display the 200 OK status code and the HTML content from index.html.

## Troubleshooting
If Port 8080 is in use, modify the `PORT` variable in both scripts to 8081.
