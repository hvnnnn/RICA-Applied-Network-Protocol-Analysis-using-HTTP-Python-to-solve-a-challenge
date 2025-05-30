# RICA-Applied-Network-Protocol-Analysis-using-HTTP-Python-to-solve-a-challenge

This project is a solution to a Python-based brute force challenge, where the objective is to discover a 3-digit PIN code (000–999) by communicating directly with a local server using raw socket programming.

Challenge Requirements

- Guess the correct 3-digit numeric PIN by brute-forcing.
- Use only Python and the standardd `socket` library (no `requests`, `urllib`, etc.).
- Send data manually using the HTTP POST method.
- Identify success when the server responds with "Access Granted".

How It Works

The script:
1. Iterates over all possible 3-digit PINs from `000` to `999`.
2. Connects to the server at `127.0.0.1:8888` using the socket library.
3. Sends a raw HTTP POST request with the body `magicNumber=PIN`.
4. Reads and checks the server's response for the phrase `"Access Granted"`.
5. Stops when the correct PIN is found.

What I Learned

- How to build a manual HTTP POST request using raw sockets.
- How brute-force attacks work against login endpoints.
- Importance of rate-limiting and input validation on the server side.
- How to use Git and GitHub for version control and documentation.

Security Reflection

To prevent this kind of brute-force attack, a real-world system should:
- Implement rate-limiting and lockouts on failed attempts.
- Require CAPTCHAs or 2FA after several wrong tries.
- Log and monitor suspicious behavior (e.g., repeated login failures).
- Avoid giving detailed response messages that indicate success/failure.

How to Run

Make sure local server is running on `127.0.0.1:8888`, then:

```bash
python crackingthecode.py
