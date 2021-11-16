import socket

def main():

    # Establish INET, STREAMing socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to socket's hostname & port 80
    server_socket.bind((socket.gethostname(), 80))

    # Listen for one connection
    server_socket.listen(1)

    while True:

        # Accept connections from outside
        (c, address) = server_socket.accept()
        client_socket = c

        checking_connection = True

        # If we accepted a socket
        if client_socket is not None and checking_connection:
            print("Connection Succeeded")
            checking_connection = False

        # Get input for message
        msg_to_send = bytes(input(">"), 'utf-8')
        client_socket.send(msg_to_send)


main()