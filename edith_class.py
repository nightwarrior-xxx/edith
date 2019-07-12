#! /usr/bin/env python3

import socket

irc = socket.socket()

class help_edith:

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def send_message(self, channel, message):
        self.irc.send(bytes("PRIVMSG " + channel + " :" + message + "\n", "UTF-8"))
    
    def connect(self, server, port, channel, botname):
        self.irc.connect((server, port))
        self.irc.send(bytes("USER " + botname + " " + botname + " " + botname + ": I am edith\n", "UTF-8"))
        self.irc.send(bytes("NICK " + botname + " \n", "UTF-8"))
        self.irc.send(bytes("JOIN " + channel + " \n", "UTF-8"))
        
    def get_message(self):
        msg = self.irc.recv(4096).decode("UTF-8")
        if msg.find('PING') != -1:
            print(msg.find('PING'))                      
            self.irc.send(bytes("PONG :pingis\n", "UTF-8"))
            print("message has been sent !!")
        return msg

    def stop(self):
        self.irc.send(bytes("QUIT \n", "UTF-8"))
        print('Edith is going down !!')