import socket

def client_connect(ip, port):

    try:
        # Establish connection socket
        x = socket.socket()

        # Connect
        x.connect((ip, port))

    except Exception as e:
        print(e)


def main():


    # Establish ip to connect to
    ip = "10.0.2.6"

    # Get user input for port number as int
    port = int(input("Please enter your port number:"))

    # Get user input for admin's name
    admin_name = input("Please enter the admin's name:")

    # Connect using ip and port
    client_connect(ip, port)


main()