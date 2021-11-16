import socket
from _thread import *
import threading

print_lock = threading.Lock()


def threaded(client_socket, admin_name):
    while True:

        # Receive messages up to 1024 bytes
        received_msg = client_socket.recv(1024)

        if not received_msg:
            print("BYE!")

            #release lock and exit
            print_lock.release()
            break

        print(received_msg.decode('utf-8'))

        # Send messages
        # Get input for message, append admin name (capitalized) to front, and convert to bytes
        username = admin_name.upper() + ": "
        msg_to_send = bytes(username + input(), 'utf-8')
        client_socket.send(msg_to_send)

def server_connect(ip, port, admin_name):
    # Establish socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow reuse of socket
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind socket to ip and port of THIS machine
    server.bind((ip, port))

    # Listen for one connection
    server.listen(1)

    # Loop until client exits
    while True:
        # Accept connections from outside
        (client_socket, address) = server.accept()

        # lock client
        print_lock.acquire()

        # Msg if connection succeeds
        print("Connected to:", address)

        # Begin new thread
        start_new_thread(threaded, (client_socket, admin_name,))





def main():
    # Establish ip of self for binding (Switch comments to test on local machine vs VMs)
    ip = "10.0.2.6"
    # ip = "127.0.0.1"

    # Get user input for port number as int
    port = 8080 #int(input("Please enter your port number: "))

    # Get user input for admin's name
    admin_name = "Alice" #input("Please enter the admin's name: ")

    # Connect using ip and port
    server_connect(ip, port, admin_name)


main()
