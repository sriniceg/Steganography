#client
from socket import *
from threading import *
from tkinter import *
import user1
import user2

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "127.0.0.1"
portNumber = 7500

clientSocket.connect((hostIp, portNumber))

window = Tk()
window.title("Connected To: "+ hostIp+ ":"+str(portNumber))

txtMessages = Text(window, width=50)
txtMessages.grid(row=0, column=0, padx=10, pady=10)

txtYourMessage = Entry(window, width=50)
txtYourMessage.insert(0,"Your message")
txtYourMessage.grid(row=1, column=0, padx=10, pady=10)

def sendMessage():
    clientMessage = txtYourMessage.get()
    x  = clientMessage.split()
    image = x[0]
    data = " ".join(x[1:])
    obj = user1.Steganography()
    obj.getimage(image,data)
    txtMessages.insert(END, "\n" + "You: "+ data)
    clientSocket.send(obj.send().encode())

btnSendMessage = Button(window, text="Send", width=20, command=sendMessage)
btnSendMessage.grid(row=2, column=0, padx=10, pady=10)

def recvMessage():
    while True:
        serverMessage = clientSocket.recv(100000).decode()
        obj2 = user2.Steganography()
        txtMessages.insert(END, "\n"+obj2.receive(serverMessage))

recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()

window.mainloop()
