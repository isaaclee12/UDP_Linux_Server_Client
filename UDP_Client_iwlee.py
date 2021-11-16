import socket


def client_connect(ip, port, client_name):
    try:
        # Establish INET, STREAMing socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Attempt connection to an ip
        client_socket.connect((ip, port))

        print("Connected to:", ip)

        while True:
            # Get input for message, append client name to front, and convert to bytes
            client_socket.sendall(bytes(client_name + ":" + input(">"), 'utf-8'))

            # Receive messages up to 1024 bytes
            print("CLIENT:", client_socket.recv(1024))

    except Exception as e:
        print(e)


def main():
    # Establish ip to connect to
    ip = "10.0.2.6"

    # Get user input for port number as int
    port = int(input("Please enter your port number:"))

    # Get user input for admin's name
    client_name = input("Please enter the client's name:")

    # Connect using ip and port
    client_connect(ip, port, client_name)


main()
