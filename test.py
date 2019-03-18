import socket
import sys
import time
from tkinter import *
import tkinter as tk
import threading

def messagesent(mess,n):
    messageVar = Message(root, text = mess, width=1000) 
    messageVar.config(bg='red') 
    messageVar.pack(fill=X)
def messagerecv(mess,n):
    messageVar = Message(root, text = mess, width=1000) 
    messageVar.config(bg='yellow') 
    messageVar.pack(fill=X)

def go_online():
    global ip
    s=socket.socket()
    host=socket.gethostname()
    print("\nserver will start on host: ",host);
    port=8080
    s.bind((host,port))
    print('\a')
    print("server done binding to host and port successfully")
    print("server is waiting for incoming connections \n")
    s.listen(1)
    conn, addr=s.accept()
    ip=conn
    print(addr,"is now connected to the server and is now online...")
    
    ourMessage ='You are now connected'
    messageVar = Message(root, text = ourMessage, width=1000) 
    messageVar.config(bg='lightgreen') 
    messageVar.pack(fill=X)
    #refreshnow(n)

def retrieve_input(line):
    
    inputValue=textBox.get("1.0","end-1c")
    messagesent(inputValue,line)
    inputValue=inputValue+'\n'
    inputValue=inputValue.encode()
    ip.send(inputValue) 
    global n
    n=n+1
    print("kg: ",incoming_message)

def refreshnow(line):
    threading.Timer(5.0, refreshnow).start()
    incoming_message = ip.recv(1024)
    print(incoming_message)
    incoming_message = incoming_message.decode()
    messagerecv(incoming_message,line)
    global n
    n=n+1
    print("kg: ",incoming_message)
    

    

#window
root = tk.Tk()
root.geometry("300x700")
root.title("Toddy")


frame = tk.Frame(root)
frame.pack()



#buttons
online=tk.Button(frame,text="GO ONLINE", fg="red",command=go_online)
online.pack(fill=X)

button = tk.Button(frame,text="QUIT", fg="red",command=quit)
button.pack(fill=X)


textBox=Text(frame, height=2, width=25, bg="grey")
textBox.pack(fill=X)


n=6
buttonCommit=tk.Button(frame, height=1, width=10, text="Send",command=lambda: retrieve_input(n))
buttonCommit.pack(fill=X)


refresh=tk.Button(frame, height=1, width=10, text="Refresh",command=lambda: refreshnow(n))
refresh.pack(fill=X)


root.mainloop()