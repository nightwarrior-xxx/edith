#! /usr/bin/env python3

from edith_class import *
from meetup_details import next_events_links, links

server = "irc.freenode.net"
port = 6667
botname = "edith_"
botnickpass = "iamironman"
botpass = "tonystark"
channel = "#testedith"
admin_name = ['nightwarrior-xxx']
users = [
'ryzokuken', 'sidntrivedi012', 'nightwarrior-xxx','rogers_'
'shermisaurus','weirdwiz'
]

irc = help_edith()

irc.connect(server, port, channel, botname)


while True:
    msg = irc.get_message()
    print(msg)
    try :

        if "PRIVMSG" in msg and channel in msg:
            real_msg = msg.split('PRIVMSG')[1].split(':')[1]
            name = msg.split('!')[0][1:]           

            if name not in users:
                welcome_msg = "Welcome {name} to the IRC channel of OSDC. You are save here from NSA".format(name=name)
                irc.send_message(channel, welcome_msg)
                print('-------Welcome message send-----------')
                users.append(name)

            if real_msg.find("fuck") != -1 or \
                real_msg.find("asshole") != -1 or \
                real_msg.find("ass") != -1 or \
                real_msg.find("bitch") != -1 or \
                real_msg.find("fuckoff") != -1 or \
                real_msg.find("motherfucker") != -1:
                
                warn_msg = "This is warning {name}, next time you will kicked out.".format(name=name)
                irc.send_message(channel, warn_msg)
                print('----------warning sent-------------')


            elif real_msg.find("#edith") != -1 :
                message  = "Hello {name}. You are save here from NSA. How can I help you ?".format(name=name)
                irc.send_message(channel, message)
                print('----------message send---------------')

            elif real_msg.find("#stopedith") != -1:
                if name in admin_name:
                    irc.send_message(channel, "I am going for a sleep. But I will be back soon. Till then save your ass from NSA")
                    irc.stop()

            elif real_msg.find('#upcomingevents') != -1:
                l = links()
                l.get_events_links()
                for i in next_events_links:
                    irc.send_message(channel, "- "+i)
                print('------------Links send----------- ')

    except Exception:
        print('Something is wrong. Also NSA is watching you !!')
