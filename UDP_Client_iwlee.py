import socket
import sys
from requests import get


def recieve(sock):
    # Infinite loop while recieving messages
    while (1):
        try:
            output = sock.recv(500)
            print(output)


def main():
    # Establish ip to connect to
    ip = "10.0.2.6"

    # Get user input for port number as int
    port_number = int(input("Please enter your port number:"))

    # Get user input for admin's name
    admin_name = input("Please enter the admin's name:")

    # Connect using the inputted port
    # try:

    # Establish connection socket
    x = socket.socket()

    # Connect
    x.connect((ip, port_number))

    # Listen for up to 1 connection
    # x.listen(1)

    # Record data if a connection is accepted
    # sock,b=x.accept()

    # Connection succeeded message
    print("Successfully connected on UDP port", port_number)

    # Recieve and record messages
    recieve(sock)

    """
    # If the connection fails for any reason
    except:
        print("Connection failed or terminated")
        exit()
    """


main()

# OTHER

import sys
import socket


def main():
    # Establish machine ip
    ip = get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip))

    # Get user input for port number
    port_number = input("Please enter your port number:")

    # Get user input for client's name
    client_name = input("Please enter the client's name:")

    # initialize the connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port_number))
    sock.sendall("test")
    time.sleep(0.5)
    sock.shutdown(socket.SHUT_WR)
    res = ".

    while True:

        # recieve 1024 bytes
        data = sock.recv(1024)

        if (not data):
            break
            res += data.decode()
            print(res)

    print("Connection closed.")
    sock.close()


# no idea what this does
# content = "GET / HTTP/1.1\nHost: google.com\n\n"
# netcat(hostname, port, content.encode()).

main()