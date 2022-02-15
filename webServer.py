# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)  # create TCP socket
    # Prepare a server socket -
    serverSocket.bind(("", port))  # associate server port with socket
    # Fill in start
    serverSocket.listen(1)  # listen for connections .listen(queue#)
    # Fill in end

    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # create new socket on server connect to client
        try:

            try:
                message =  connectionSocket.recv(1024).decode()
                filename = message.split()[1]  # parse header of HTTP req
                f = open(filename[1:])  # open file header
                outputdata = f.read()  # read header
                # Send one HTTP header line into socket.
                # Fill in start
                serverSocket.send(outputdata.encode())
                # Fill in end

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()  # close client socket
            except IOError:
                # Send response message for file not found (404)
                # Fill in start
                connectionSocket.send("404 Not Found".encode())
                # Fill in end
                # Close client socket
                # Fill in start
                connectionSocket.close()  # close client socket
                # Fill in end

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close() # close socket
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)