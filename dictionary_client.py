import socket

def Main():
    host = '127.0.0.1'
    port = 2000
    s = socket.socket()
    s.connect((host,port))
    word = input("Enter the word (to quit('I quit')-> ")
    if word !='I quit':
        s.send(word.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print (data)
    else:
        s.close()

if __name__ == "__main__":
	Main()
