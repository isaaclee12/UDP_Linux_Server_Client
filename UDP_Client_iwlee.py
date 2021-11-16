import socket
import select
import sys

def client_connect(ip, port, client_name):
    # Establish INET, STREAMing socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Attempt connection to an ip
    client_socket.connect((ip, port))

    print("Connected to:", ip)

    while True:

        # Get input for message, append client name (capitalized) to front, and convert to bytes
        username = client_name.upper() + ": "
        msg_to_send = bytes(username + input(), 'utf-8')
        client_socket.sendall(msg_to_send)

        # Receive messages up to 1024 bytes
        print(client_socket.recv(1024).decode('utf-8'))


def main():
    # Establish ip of Alice (Switch comments to test on local machine vs VMs)
    ip = "10.0.2.6"
    # ip = "127.0.0.1"

    # Get user input for port number as int
    port = 8080 #int(input("Please enter your port number: "))

    # Get user input for admin's name
    client_name = "Bob" #input("Please enter the client's name: ")

    # Connect using ip and port
    client_connect(ip, port, client_name)


main()
