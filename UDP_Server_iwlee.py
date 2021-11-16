import socket


def server_connect(ip, port, admin_name):
    # Establish INET, STREAMing socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to socket's hostname & port 80
    server_socket.bind((socket.gethostname(), 80))

    # Listen for one connection
    server_socket.listen(1)

    # Accept connections from outside
    (client_socket, address) = server_socket.accept()

    # Msg if connection succeeds
    with client_socket:
        print("Connected to:", address)

        while True:
            # Receive messages up to 1024 bytes
            received_msg = client_socket.recv(1024)
            print("CLIENT:", received_msg)

            # Send messages
            # Get input for message, append admin name to front, and convert to bytes
            msg_to_send = bytes(admin_name + ":" + input(">"), 'utf-8')
            client_socket.send(msg_to_send)


def main():
    # Establish ip to connect to
    ip = "10.0.2.5"

    # Get user input for port number as int
    port = int(input("Please enter your port number:"))

    # Get user input for admin's name
    admin_name = input("Please enter the admin's name:")

    # Connect using ip and port
    server_connect(ip, port, admin_name)


main()
