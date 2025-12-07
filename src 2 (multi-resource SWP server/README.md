
````markdown
# SWP/1.0 Web Server – Execution Guide

## Requirements
- Python 3.x  
- No external libraries required  
- Ensure all static files are inside the `www` directory.

---

## How to Run

### 1. Start the Server
Open a terminal in the `src` folder and run:

```bash
python swp_server.py
````

You should see:

```
SWP/1.0 Server running on 127.0.0.1:8080
```

### 2. Start the Client

Open a second terminal and run:

```bash
python swp_client.py
```

The client will send a GET request (e.g., `/index.html`) to the server.

---

## Expected Output

### Server Output

* Logs each incoming request
* Shows the requested resource
* Sends back status codes:

  * `200 OK` if the file exists
  * `404 Not Found` if missing

### Client Output

* Displays the SWP response
* Shows received HTML/CSS/JS content
* Confirms status line & content length

---

## Project File Structure

```
src/
│
├── swp_server.py
├── swp_client.py
│
└── www/
     ├── index.html
     ├── about.html
     ├── css/
     │     └── style.css
     ├── js/
     │     └── app.js
     └── images/
           └── logo.png
```

---

## Troubleshooting

### Port Already in Use

Change port in both scripts:

```python
PORT = 8081
```


## Notes

* Server uses **non-persistent TCP** (one request per connection)
* Fully follows the custom **SWP/1.0 protocol** created for this assignment
