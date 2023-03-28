import telnetlib
import time

# Connection settings
host = "192.168.1.187"
port = 30000  # The default grandma2 telnet port
timeout = 10  # Set a timeout for the connection

# Connect to the console
telnet = telnetlib.Telnet(host, port, timeout)
print(f"Connected to: {host}:{port}")
telnet.read_until(b"[Fixture]>")
telnet.write(b"\n")
time.sleep(0.5)


def send_command(command):
    
    telnet.write(command.encode('ascii') + b'\r\n')
    time.sleep(0.5)  # Add a delay to allow the console to process the command
    response = telnet.read_very_eager().decode('ascii')
    print(f"Command: {command}\nResponse: {response}")
    return response

# Replace these example commands with your actual commands
commands = [
    "login administrator admin\n",
    "fixture 1703 attribute \"Pan\" at 97",
    "fixture 1703 attribute \"Tilt\" at 25",
]

for command in commands:
    send_command(command)

# Close the connection
telnet.close()
print("Connection closed.")
