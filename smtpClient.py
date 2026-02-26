from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "Subject: Testing\r\n\r\nMy message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(socket.AF_INET, SOCK_STREAM)
    clientSocket.settimeout(5)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    # Fill in end

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = 'MAIL FROM:<kashika@abc.com>\r\n'
    clientSocket.send(mailFrom.encode())
    recvMailFrom = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptTo = 'RCPT TO:<kashika@xyz.com>\r\n'
    clientSocket.send(rcptTo.encode())
    recvRcptTo = clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recvData = clientSocket.recv(1024).decode()
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recvEndmsg = clientSocket.recv(1024).decode()
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    recvQuit = clientSocket.recv(1024).decode()
    # Fill in end

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')