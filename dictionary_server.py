import socket
import threading

d = {'apple': 'type of fruit', 'teacher': 'A teacher is a person who helps others to acquire knowledge',
     'tranquil': 'free from disturbance', 'baritone': 'an adult male singing voice between tenor and bass'}

def meaning(msg):
    for key, val in d.items():
        if (msg == key):
            return val
    return 0


def extractMeaning(name,sock):
    msg = sock.recv(1024).decode('utf-8')
    v = meaning(msg)
    if v != 0:
        m = "Status: Found\n"
        m1 = m+ "Meaning: "+ v
        sock.send(m1.encode('utf-8'))
    else:
        m1 = "Status: Not Found\n"
        sock.send(m1.encode('utf-8'))
    sock.close()

def Main():
	host = '127.0.0.1'
	port = 2000
	s = socket.socket()
	s.bind((host,port))
	s.listen(5)
	print ("Server Started..  ")
	while True:
		c, addr = s.accept()
		print ("client connected ip:<" + str(addr) +">")
		t = threading.Thread(target=extractMeaning, args = ("retrThread",c))
		t.start()
	s.close()

if __name__ == '__main__':

	Main()
